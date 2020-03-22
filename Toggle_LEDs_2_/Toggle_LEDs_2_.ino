//int value = 0;
int brightness = 0;
int fade = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  analogWrite(10, abs(255*sin(value/510)));
//  value = value + 2;
  analogWrite(10, brightness);
  if (brightness + fade < 0 || brightness + fade > 255) {
    fade = -fade;
  }
  brightness = brightness + fade;
  delay(30);
}
