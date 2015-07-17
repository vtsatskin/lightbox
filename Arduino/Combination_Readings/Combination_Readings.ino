#include <Wire.h>
#include <Adafruit_10DOF.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_L3GD20_U.h>
#include <Adafruit_LSM303_U.h>
#include <Adafruit_BMP085_U.h>

Adafruit_BMP085_Unified bmp = Adafruit_BMP085_Unified(10085);
Adafruit_LSM303_Mag_Unified mag = Adafruit_LSM303_Mag_Unified(10303);
Adafruit_LSM303_Accel_Unified accel = Adafruit_LSM303_Accel_Unified(11303);

const int firstPin = A0;
const int secondPin = A1;
const double smallR = 1.8;
const int bigR = 18;

void setup(void) {
  Serial.begin(9600);

  if (!bmp.begin() || !mag.begin() || !accel.begin()) {
    Serial.print("Ooops, no BMP085 or LSM303 detected");
    while(1);
  }
}

void loop() {
  sensors_event_t eventP;
  sensors_event_t eventM;
  sensors_event_t eventA;
  float temperature;

  int firstVal = analogRead(firstPin);
  int secondVal = analogRead(secondPin);
  float firstVolt = (firstVal/1024.0)*5;
  float secondVolt = (secondVal/1024.0)*5;
  double current = (firstVolt - secondVolt)/smallR;
  double power = current*current*(bigR+smallR+20);
 
  bmp.getEvent(&eventP);
  mag.getEvent(&eventM);
  bmp.getTemperature(&temperature);
  accel.getEvent(&eventA);
  
  float heading=(atan2(eventM.magnetic.y, eventM.magnetic.x)*180)/PI;
  while (heading < 0)
  {
    heading = 360 + heading; 
  }
  Serial.print("{");
  
  Serial.print("\"current\": ");  
  Serial.print(current*1000);
  Serial.print(", ");
  
  Serial.print("\"power\": ");  
  Serial.print(power,6);
  Serial.print(", ");
  
  Serial.print("\"pressure\": ");
  Serial.print(eventP.pressure);
  Serial.print(", ");
  
  Serial.print("\"temperature\": ");
  Serial.print(temperature);
  Serial.print(", ");
  
  Serial.print("\"compass\": ");
  Serial.print("[");
  Serial.print(eventM.magnetic.y);
  Serial.print(", ");
  Serial.print(eventM.magnetic.x);
  Serial.print(", ");
  Serial.print(heading);
  Serial.print("]");
  Serial.print(", ");
  Serial.print("\"accelerometer\": ");
  Serial.print("[");
  Serial.print(eventA.acceleration.x);
  Serial.print(",");
  Serial.print(eventA.acceleration.y);
  Serial.print(",");
  Serial.print(eventA.acceleration.z);
  Serial.print("]");

  Serial.print("}\n");  
  
  delay(125);
}
