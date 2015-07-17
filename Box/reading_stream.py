import serial
import logging
import sys
import json
import couchdb
import time

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

SERIAL_HANDLE='/dev/ttyACM0'
RATE=9600

logging.info("Opening connection to %s at rate of %i", SERIAL_HANDLE, RATE)
ser = serial.Serial(SERIAL_HANDLE, RATE)

couch = couchdb.Server()
readings = couch['readings']

# There is a constant stream of data coming from the Arduino. The first time
# reading may be in the middle of the stream, which would not be a valid
# json string. We'll read the first n to create a stready-state reading.
for i in range(5):
    ser.readline()

while True:
    raw = ser.readline()
    logging.debug("Raw reading: %s", raw)

    data = json.loads(raw)
    data['time'] = time.time()

    logging.debug("JSON reading: %s", data)

    readings.save(data)
