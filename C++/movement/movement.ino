#include <Servo.h>

Servo servoRight;
Servo servoLeft;

void setup() {
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}
void forward(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  delay(500); 
}

void backward(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(900);
}

void superdirection(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
  delay(900);
}
void mysteryDirection(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
  delay(500);
}

void stopServos(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
  delay(500);
}
void loop(){
  forward();
  stopServos();
  mysteryDirection();
  stopServos();
  backward();
  stopServos();
  superdirection();
  stopServos();
}

