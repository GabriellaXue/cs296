#include <SPI.h>
#include "pins_arduino.h"

void setup() {
  Serial.begin(9600);
  pinMode(MOSI, INPUT);
  pinMode(2, OUTPUT);
  // turn on SPI in slave mode
  SPCR |= _BV(SPE);
}

void loop() {
  Serial.println(digitalRead(MOSI)); 
  digitalWrite(2, digitalRead(MOSI));
  delay(500);
} 
