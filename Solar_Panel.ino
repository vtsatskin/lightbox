const int firstPin = A0;
const int secondPin = A1;
const int smallR = 270;
const int bigR = 27000;

void setup() {
  // put your setup code here, to run once:
  
  analogReference(EXTERNAL);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
int firstVal = analogRead(firstPin);
int secondVal = analogRead(secondPin);
float firstVolt = (firstVal/1024.0)*3.3;
float secondVolt = (secondVal/1024.0)*3.3;
double current = (firstVolt - secondVolt)/smallR;
double power = current*current*bigR;
Serial.print(firstVal);
Serial.print(", ");
Serial.print(secondVal);
Serial.print(", ");
Serial.print(current*1000,6);
Serial.print("mA");
Serial.print(" ");
Serial.print(power*1000,6);
Serial.print("mW \n");

}
