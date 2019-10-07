/*
This code is a demo of the code used for the telemetry transmission between the rocket's OBC and the ground station.
The purpose of this is to :
  - Provide a simple code to test the ground station software
  - Define the transmission protocol between the rocket and the ground station

Assumptions :
  - The link is unidirectionnal

Protocol description :
  Data is sent by "line" ie. by packet of data ending with a newline (line feed '\n').
  To check the integrity of the data sent (at least it's completeness), the first character is :
    - "@" for a header line
    - "#" for a data line
    - "%" for a calibration line
    - "$" for a message line
  The first character is used to check if we received the beginning of the line. The last character is used to check
  if the line is complete (ie if the serial read did not timeout before the end of the line)

  Before transmitting values, the telementry receiver sends a recognizable BONJOUR string so that the reader can
  identify what device is sending data

Comments :
  - We should send the time of the data sampling along the samples
  - The link could be bi-directionnal while the rocket is on the launch pad
  - We need to define a nomenclature between the OBC and the Dashboard to know how to process the data

*/

#define START_HEAD "@"
#define START_DATA "#"
#define START_CALI "%"
#define START_MESS "$"
#define SEP_DATA "&"
#define SEP_CALI ":"
#define END_LINE "\n"

#define BONJOUR "TELEMETRY"

// Change this to use a different baudrate
#define BAUDRATE 115200

int cpt = 0;
unsigned long time;

void setup()
{
  Serial.begin(BAUDRATE);

  bonjour();
  
  health_check();

  delay(100);
}

// Dummy code to send arbitrary data to the ground station
// The data should match the header
void loop()
{
  if (cpt >= 50)
  {
    cpt = 0;
  }
  time = millis();
  Serial.print(START_DATA);
  Serial.print(time);
  Serial.print(SEP_DATA);
  Serial.print(cpt + 1);
  Serial.print(END_LINE);
  cpt++;

  delay(10);
}

void bonjour()
{
  // Send string to indicate that this device is the telemetry receiver
  Serial.print(BONJOUR);Serial.print(END_LINE);
}

void health_check()
{
  Serial.print(START_MESS);
  Serial.print("Health check started");
  Serial.print(END_LINE);
  delay(10);
  Serial.print(START_MESS);
  Serial.print("IMU1 OK");
  Serial.print(END_LINE);
  delay(10);
  Serial.print(START_MESS);
  Serial.print("IMU2 FAILED");
  Serial.print(END_LINE);
  delay(10);
  Serial.print(START_MESS);
  Serial.print("Sending calibration data ...");
  Serial.print(END_LINE);
  delay(10);
  calibration();
  delay(10);
  Serial.print(START_MESS);
  Serial.print("Sending calibration data done");
  Serial.print(END_LINE);
  delay(10);
  Serial.print(START_MESS);
  Serial.print("Sending header data ...");
  Serial.print(END_LINE);
  delay(10);
  header();
  delay(10);
  Serial.print(START_MESS);
  Serial.print("Sending header data done");
  Serial.print(END_LINE);
  delay(10);
  Serial.print(START_MESS);
  Serial.print("Health check complete");
  Serial.print(END_LINE);
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