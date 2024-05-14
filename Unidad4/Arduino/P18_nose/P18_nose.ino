#include "Servo.h"
int pinServo=9;
Servo servo;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(pinServo);

}

void loop() {
  // put your main code here, to run repeatedly:
  servo.write(0);
  Serial.println("servo en 0 grados");
  delay(500);

  servo.write(180);
  Serial.println("servo en 180 grados");
  delay(500);

  
}
