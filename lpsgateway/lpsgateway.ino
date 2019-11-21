/* Embedded software for the Launch Pad Station

/!\ Power the Launch Pad Station Board BEFORE powering the relays /!\

This code receives commands from a LoRa module RFM9XW and controls the rocket fuel sequence
Commands are also forwarded to the rocket itself using logic levels on single wires

This is tested on Arduino Nano 3.0 boards

Hardware :
  - 1x Arduino Nano
  - 1x RFM9xW LoRa tranceiver
  - 3x Relay
  - 1x Rocket

Wiring :
                Arduino      RFM95/96/97/98
                GND----------GND   (ground in)
                3V3----------3.3V  (3.3V in)
interrupt 0 pin D2-----------DIO0  (interrupt request out)
                D9-----------RESET (reset pin)
         SS pin D10----------NSS   (CS chip select in)
        SCK pin D13----------SCK   (SPI clock in)
       MOSI pin D11----------MOSI  (SPI Data in)
       MISO pin D12----------MISO  (SPI Data out)
                Connect everything through level shifters 5V <-> 3V3
                The RFM9XW are 3V3 logic and are NOT 5V tolerant

                Arduino      Rocket
                GND----------GND   (ground in)
                A0-----------Ombilical 1 (Telemetry/FPV enable)
                A1-----------Ombilical 2 (Calibration start)

                Arduino      Ignition Relay
                GND----------GND   (ground in)
                A2-----------IN1   (Command pin)
                5V-----------VCC   (5V in)
                Connect the ignition circuit on Normally Open side

                Arduino      FILL/VENT Relay (NB: jumper between VCC and JD-VCC)
                GND----------GND   (ground in)
                A3-----------IN2   (Command pin for relay 2)
                A4-----------IN1   (Command pin for relay 1)
                5V-----------VCC   (5V in)
                Connect the solenoids on Normally Open side
*/

// Including  RadioHead library 
#include <SPI.h>
#include <RH_RF95.h>
#include <RHReliableDatagram.h>

// Single wire ombilicals to the rocket
#define PIN_OMBI_TM A0 // Write LOW to this pin to disable the Telemetry and FPV transmitters
#define PIN_OMBI_CA A1 // Write LOW to this pin to start a sensor calibration on the rocket
// Pins where the relays are connected
#define PIN_RELAY_FIRE A2 // Write LOW to this pin to enable the ignition circuit
#define PIN_RELAY_FILL A3 // Write LOW to this pin to open solenoid 1
#define PIN_RELAY_VENT A4 // Write LOW to this pin to open solenoid 2

#define CMD_FILL_START 0x61 // 'a'
#define CMD_FILL_STOP  0x62 // 'b'
#define CMD_VENT_START 0x63 // 'c'
#define CMD_VENT_STOP  0x64 // 'd'
#define CMD_ARM        0x65 // 'e'
#define CMD_DISARM     0x66 // 'f'
#define CMD_FIRE_START 0x67 // 'g'
#define CMD_FIRE_STOP  0x68 // 'h'
#define CMD_TM_ENABLE  0x41 // 'A'
#define CMD_TM_DISABLE 0x42 // 'B'
#define CMD_CA_TRIGGER 0x43 // 'C'

#define BAUDRATE 115200
#define BONJOUR 'LAUNCHPADSTATION'
#define RFM95_CS 10
#define RFM95_RST 9
#define RFM95_INT 2
#define RF95_FREQ 915.0

RH_RF95 rf95(RFM95_CS, RFM95_INT);

uint8_t command = 0x00;
bool is_filling = false;
bool is_venting = false;
bool is_armed = false;

uint8_t rf95_buf[RH_RF95_MAX_MESSAGE_LEN]; // rf95.maxMessageLength()Or [RH_RF95_MAX_MESSAGE_LEN]
uint8_t rf95_len = sizeof(rf95_buf);
uint8_t ser_command = 0;
uint8_t rfm_command = 0;

void setup()
{
  pinMode(PIN_RELAY_FIRE, OUTPUT);
  pinMode(PIN_RELAY_FILL, OUTPUT);
  pinMode(PIN_RELAY_VENT, OUTPUT);
  pinMode(PIN_OMBI_TM, OUTPUT);
  pinMode(PIN_OMBI_CA, OUTPUT);
  // Disable the ignition circuit
  digitalWrite(PIN_RELAY_FIRE, HIGH);
  // Close the solenoids
  digitalWrite(PIN_RELAY_FILL, HIGH);
  digitalWrite(PIN_RELAY_VENT, HIGH);
  // Default state is HIGH for the ombilicals
  digitalWrite(PIN_OMBI_TM, HIGH);
  digitalWrite(PIN_OMBI_CA, HIGH);
  // Reset of RFM95
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);
  
  init_communication();
}

void loop()
{
  ser_read_byte(&ser_command);
  rfm_read_byte(&rfm_command);
  
  if (ser_command)
  {
    rfm_send_byte(&ser_command);
  }
  if (rfm_command)
  {
    ser_send_byte(&rfm_command);
  }
  
  // Reset this to the default value
  ser_command = 0x00;
  rfm_command = 0x00;
  delay(100);
}

/*
 * Functions for communication with the Ground Station
 */

void init_communication()
{ // Initialize the communication link
  Serial.begin(BAUDRATE);
  Serial.println(BONJOUR);
  
  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }
  Serial.println("LoRa radio init OK!");
 
  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  Serial.print("Set Freq to: "); Serial.println(RF95_FREQ);

  // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on
 
  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then 
  // you can set transmitter powers from 5 to 23 dBm:
  rf95.setTxPower(23, false);
}

void ser_read_byte(uint8_t *serial_data)
{ // Read one byte in the serial buffer
  if (Serial.available() > 0)
  {
    *serial_data = Serial.read();
    Serial.write("Read command..");
  }
}

void rfm_read_byte(uint8_t *rfm_data)
{ // Read one byte in the rfm buffer
  /*if (rf95.available())
  {
    rf95.recv(buf, &len);
    *rfm_data = *buf;
  }*/
  if (rf95.recv(rf95_buf, &rf95_len))
  {
    *rfm_data = rf95_buf[0];
    Serial.write("Received from LPS");
  }
}

void ser_send_byte(uint8_t *data)
{ // Write one byte to the communication link
  Serial.write(*data);
}

void rfm_send_byte(uint8_t *data)
{
  rf95.send(*data, 1);   //Make sure later that len in .send(data, len) is big enought for data.
  Serial.write("Sending to LPS..");
}
