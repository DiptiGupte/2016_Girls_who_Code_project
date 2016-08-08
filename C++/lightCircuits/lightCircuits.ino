int LEDPIN = 4;
int LEDPIN2 = 5;

void setup() {
  // put your setup code here, to run once: 
  pinMode(LEDPIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LEDPIN,HIGH);
  digitalWrite(LEDPIN2, LOW);
  delay(1000);
  digitalWrite(LEDPIN, LOW);
  digitalWrite(LEDPIN2, HIGH);
  delay(1000);   
}
