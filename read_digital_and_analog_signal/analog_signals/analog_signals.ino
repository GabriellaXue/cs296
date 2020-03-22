int analogPin = A0;

double val = 0;

void setup() {
   Serial.begin(9600);
   // Set pin 6 as output
   pinMode(6, OUTPUT);
}

void loop() {
  // Read the value from A0
  val = analogRead(analogPin);
  // Convert the interger result into voltage
  double volt = val * 5 / 1024;
  Serial.println(volt);
  // Make Led light dim as changing the voltage
  analogWrite(6, 255*volt/5);
  Serial.println(255*volt/5);
}
