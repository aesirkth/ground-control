/*
This code is a demo of how the data transmission works between the Ground Station Computer and the Rocket systems:

    Telemetry is received in real time from the Rocket on the Ground Station Computer via a downlink telemetry transmitter
    This link is unidirectional
    
    Commands are sent from the Ground Station to the Launch Pad Station
    This link is bidirectional

In the real world:
    - The Rocket and the Ground Station Computer are connected through a telemetry transmitter and a telemetry receiver
    - The Launch Pad Station and the Ground Station Computer are connected through two wireless tranceivers

On the Ground Station Computer side, two Arduino boards are used as a gateways to the wireless tranceiver (from the LPS)
and to the wireless receiver (from the Rocket). The Arduino boards are connected to the computer via USB for power 
supply and serial link transmission

This code simulates a gateway to the Rocket or to the Launch Pad System and feeds fake data to the Ground Station Computer
to be used for development/testing purposes
*/

// Uncomment one of these to select the target gateway
// #define lps
#define telemetry

// Change this to use a different baudrate
#define BAUDRATE 115200

// Definition of the separators for the transmission protocol
#define START_HEAD "@"
#define START_DATA "#"
#define START_CALI "%"
#define START_MESS "$"
#define SEP_DATA "&"
#define SEP_CALI ":"
#define END_LINE "\n"

#if defined(telemetry)
    #define BONJOUR "TELEMETRY"
#elif defined(lps)
    #define BONJOUR "LAUNCHPADSTATION"
#endif

#ifdef telemetry
  uint32_t cpt = 0;
  uint32_t time;
#endif
#ifdef lps
  char command;
#endif


/* 
 * Main Arduino loops
 */


void setup()
{
  Serial.begin(BAUDRATE);

  // This is sent by the gateway immediately after initialization
  bonjour();
  // Everything after this is a simulation of what is received by the telemetry receiver/lps
  // and forwarded to the Dashboard
  
  #if defined(telemetry)
    health_check();
  #elif defined(lps)
    // health_check();
  #endif
  
  delay(100);
}

void loop()
{
  #if defined(telemetry)
    // Dummy code to send arbitrary data to the ground station
    fake_telemetry(&cpt);
  #elif defined(lps)
    // Simple ping-pong. Every byte received is sent back inside a message frame
    fake_lps();
  #endif
}


/* 
 * Common functions
 */


void bonjour()
{ // Send a string to indicate who is this device
  Serial.print(BONJOUR);Serial.print(END_LINE);
}

void send_message(char *message)
{
  Serial.print(START_MESS);
  Serial.print(message);
  Serial.print(END_LINE);
}


/* 
 * Functions for the telemetry gateway
 */


#ifdef telemetry
void send_data(uint32_t data[])
{
  Serial.print(START_DATA);
  for (byte i = 0; i < sizeof(data); i++) {
    if (i != 0)
    {
        Serial.print(SEP_DATA);
    }
    Serial.print(data[i]);
  }
  Serial.print(END_LINE);
}

void fake_telemetry(uint32_t *cpt)
{
  if (*cpt >= 50)
  {
    *cpt = 0;
  }
  time = millis();
  
  uint32_t data[2] = {time, *cpt};
  *cpt = *cpt + 1;
  send_data(data);

  delay(10);
}

void health_check()
{
  send_message("Health check started");
  send_message("IMU1 OK");
  send_message("IMU2 FAILED");
  send_message("Sending calibration data ...");
  calibration();
  send_message("Sending calibration data done");
  send_message("Sending header data ...");
  header();
  send_message("Sending header data done");
  send_message("Health check complete");
}

void calibration()
{
  Serial.print(START_CALI);
  Serial.print("BMP280_dig_T1");Serial.print(SEP_CALI);Serial.print("123456");
  Serial.print(SEP_DATA);
  Serial.print("BMP280_dig_T2");Serial.print(SEP_CALI);Serial.print("654321");
  Serial.print(END_LINE);
}

void header()
{
  // Send the header to the ground station
  Serial.print(START_HEAD);
  Serial.print("Millis");
  Serial.print(SEP_DATA);
  Serial.print("Data");
  Serial.print(END_LINE);
}
#endif


/* 
 * Functions for the lps gateway
 */


#ifdef lps
void fake_lps()
{
  while (Serial.available() > 0)
  {
    get_command(&command);
    char message = (char)command; 
    send_message(&message); // This is a dirty solution but I get strange output while using command
  }
}

void get_command(char *command)
{
  *command = Serial.read();
}
#endif