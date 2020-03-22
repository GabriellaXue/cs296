const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin 
 
void setup() {
  // initialize the led pain as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  
   // read the input on analog pin 0:
  int sensorValue = analogRead(A5);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  Serial.println(voltage);
  
  int counter = 0;
  while(digitalRead(buttonPin) == HIGH) {
    counter++;
    Serial.println(voltage);
  }
  if (counter > 100 && counter < 300) {
    if (digitalRead(ledPin) == HIGH) {
      digitalWrite(ledPin, LOW);
    } else {
      digitalWrite(ledPin, HIGH);
    }
  }
}
