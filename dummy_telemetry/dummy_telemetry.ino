/*
This code is a demo of the code used for the telemetry transmission between the rocket's OBC and the ground station.
The purpose of this is to :
  - Provide a simple code to test the ground station software
  - Define the transmission protocol between the rocket and the ground station

Assumptions :
  - The link is unidirectionnal

Protocol description :
  Data is sent by "line" ie. by packet of data ending with a newline (carriage return + line feed on Windows '\r\n').
  To check the integrity of the data sent (at least it's completeness), the first character is :
    - "H" for a header line
    - "N" for any other line
  and the last character (before the newline) is always "E".
  The first character is used to check if we received the beginning of the line. The last character is used to check
  if the line is complete (ie if the serial read did not timeout before the end of the line)

  Before transmitting values, the telementry receiver sends a recognizable BONJOUR string so that the reader can
  identify what device is sending data

  The transmission starts by the sending of the data header line to the ground station. This header is sent once.
  Then the data is sent

Comments :
  - We should send the time of the data sampling along the samples
  - The link could be bi-directionnal while the rocket is on the launch pad
  - We need to define a nomenclature between the OBC and the Dashboard to know how to process the data

*/

#define NEWLINE "N"
#define NEWHEAD "H"
#define ENDLINE "E"
#define SEPDATA "\t"
#define BONJOUR "TELEMETRY"

// Change this to use a different baudrate
#define BAUDRATE 115200


int cpt = 0;
unsigned long time;


void setup() {
  Serial.begin(BAUDRATE);
  // Send string to indicate that this device is the telemetry receiver
  Serial.println(BONJOUR);
  // Send the header to the ground station
  Serial.print(NEWHEAD);
  Serial.print("Millis");Serial.print(SEPDATA);
  Serial.print("Data");
  Serial.println(ENDLINE);

  delay(1000);
}

// Dummy code to send arbitrary data to the ground station
// The data should match the header
void loop() {
  if (cpt >= 50)
  { 
    cpt = 0;
  }
  time = millis();
  Serial.print(NEWLINE);
  Serial.print(time);Serial.print(SEPDATA);
  Serial.print(cpt + 1);
  Serial.println(ENDLINE);
  cpt++;

  delay(10);

}