#include <Adafruit_10DOF.h>

#include <Adafruit_Sensor.h>

#include <Adafruit_LSM303_U.h>

#include <Adafruit_L3GD20_U.h>

#include <Adafruit_BMP085_U.h>

void setup(void) {
  Serial.begin(9600);
  Serial.println("Pressure Sensor Test");
  Serial.println("");

  if (!bmp.begin())
  {
    Serial.print("Ooops, no BMP085 detected);
    while(1);
  }
}
void loop() {
  sensors_event_t event;
  bmp.getEvent(&event);
  if (event.pressure)
  {
    Serial.print("Pressure: ");
    Serial.print(event.pressure);
    Serial.println(" hPa.");
  }
  else
  {
    Serial.println("Sensor error.");
  }
  delay(250);
}
