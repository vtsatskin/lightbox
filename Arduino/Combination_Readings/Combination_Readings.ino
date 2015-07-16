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

void displaySensorDetails(void)
{
  sensor_t sensor;
  accel.getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" m/s^2");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" m/s^2");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" m/s^2");  
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}

void setup(void) {
  Serial.begin(9600);
  Serial.println("Sensor Test");
  Serial.println("");
  
  displaySensorDetails();

  if (!bmp.begin() || !mag.begin() || !accel.begin())
  {
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

  Serial.print("Solar Panel Current: ");  
  Serial.print(current*1000,6);
  Serial.println("mA");
  
  Serial.print("Solar Panel Power: ");  
  Serial.print(power,6);
  Serial.println("W");
 
    if (eventP.pressure)
  {
    Serial.print("Pressure: ");
    Serial.print(eventP.pressure);
    Serial.println(" hPa.");
  }
  else
  {
    Serial.println("Error: Pressure sensor");
  }
  if (temperature)
  {
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C.");
  }
  else
  {
    Serial.println("Error: Temperature sensor");
  }
   if (heading)
  {
    Serial.print("Compass Heading: ");
    Serial.print(eventM.magnetic.y);
    Serial.print(", ");
    Serial.print(eventM.magnetic.x);
    Serial.print(", ");
    Serial.print(heading);
    Serial.print("\n");
  }
  else
  {
    Serial.println("Error: Compass sensor");
  }
  
  if (1)
  {
    Serial.print("X Acceleration: ");
    Serial.print(eventA.acceleration.x);
    Serial.println(" m/s^2, ");
    Serial.print("Y Acceleration: ");
    Serial.print(eventA.acceleration.y);
    Serial.println(" m/s^2, ");
    Serial.print("Z Acceleration: ");
    Serial.print(eventA.acceleration.z);
    Serial.println(" m/s^2.");
    Serial.print("\n");
  }
  else
  {
    Serial.println("Error: Accelerometer sensor");
  }
    
   delay(1000);
  
}
