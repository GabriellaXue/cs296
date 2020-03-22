int ledPin = PD5;

void setup() {
  // set LED pin to be output
  //DDRD = B00100000;
  // |= is the compound bitwise OR operator
  // return 1 if have 1
  DDRD |= (1 << ledPin);
  Serial.begin(9600);
  
}

void loop() {
  // ^= is the XOR operator
  // different return 1 and same return 0
  PORTD ^= (1 << ledPin);
//  PORTD = B00000000;
  Serial.println(PORTD);
  delay(500);
//  PORTD = B00100000;
//  Serial.println(PORTD);
//  delay(500);
}
