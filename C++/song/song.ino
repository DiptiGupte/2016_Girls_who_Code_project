int PIEZOPIN = 6;

// One octave of notes between A4 and A5
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

int note_A5 = note_A4 * 2;
int note_As5 = note_As4 * 2; int note_Bb5 = note_As5;
int note_B5 = note_B4 * 2;

int note_rest = -1;

// note lengths defined here
long whole_note = 1600; // change tempo by changing duration of one measure
long half_note = whole_note / 2;
long quarter_note = whole_note / 4;
long eighth_note = whole_note / 8;
long sixteenth_note = whole_note / 16;

// WRITE YOUR SONG HERE
int dictionary[17][3] ={
  {6, note_G5, 400},
  {6, note_D5, 400},
  {6, note_C5, 800},
  {6, note_G5, 400},
  {6, note_D5, 400},
  {6, note_C5, 800},
  {6, note_C5, 400},
  {6, note_C5, 400},
  {6, note_C5, 400},
  {6, note_C5, 400},
  {6, note_D5, 400},
  {6, note_D5, 400},
  {6, note_D5, 400},
  {6, note_D5, 400},
  {6, note_G5, 400},
  {6, note_D5, 400},
  {6, note_C5, 800}

};

// if you want there to be silence between notes,
//   staccato should be true
bool staccato = true;

void setup() {
  pinMode(PIEZOPIN, OUTPUT);
}

void loop() {
  digitalWrite(6, HIGH);
  //PLAY YOUR SONG HERE
  for (int i = 0; i < 3; i++){
    tone(dictionary[i][0], dictionary[i][1]);
    delay(dictionary[i][2]);
  }
  
} 

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
