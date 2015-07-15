const int firstPin = A0;
const int secondPin = A1;
const double smallR = 1.8;
const int bigR = 18;

void setup() {
  // put your setup code here, to run once:
  
  //analogReference(EXTERNAL);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
int firstVal = analogRead(firstPin);
int secondVal = analogRead(secondPin);
float firstVolt = (firstVal/1024.0)*5;
float secondVolt = (secondVal/1024.0)*5;
double current = (firstVolt - secondVolt)/smallR;
double power = current*current*(bigR+smallR);
Serial.print(firstVal);
Serial.print(", ");
Serial.print(secondVal);
Serial.print(", ");
Serial.print(firstVolt);
Serial.print(", ");
Serial.print(secondVolt);
Serial.print(", ");
Serial.print(firstVolt - secondVolt);
Serial.print(", ");
Serial.print(smallR);
Serial.print(", ");
Serial.print(current*1000,6);
Serial.print("mA");
Serial.print(" ");
Serial.print(power,6);
Serial.print("W \n");

}
