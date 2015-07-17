import logging
import sys
import serial
import json
import couchdb
import time
import datetime
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure

username = ''
api_key = ''
stream_token = ''

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

stream = py.Stream(stream_token)
stream.open()

layout = Layout(
    title='Raspberry Pi Streaming Sensor Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

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

    stream.write({'x': datetime.datetime.now(), 'y': data['accelerometer'][0]})
