int cpt = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (cpt >= 10)
  { 
    cpt = 0;
  }
  
  Serial.print("N");Serial.println(cpt);
  cpt++;
  delay(1000);

}