#include <SPI.h>
#include "pins_arduino.h"


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(MOSI, OUTPUT);
  SPI.setDataMode(SPI_MODE1);
  digitalWrite(SS, HIGH); // disable Slave Select
  SPI.begin ();
  SPI.setClockDivider(SPI_CLOCK_DIV8);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(SS, LOW);
  for (int i = 0; i < 2; i++) {
    SPI.transfer(i);
    //delay(20);
  }
  digitalWrite(SS, HIGH);
  
}
