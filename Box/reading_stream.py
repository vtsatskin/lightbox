#!/usr/bin/python
import logging
import sys
import serial
import json
import couchdb
import time
import datetime
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure, YAxis
import argparse

parser = argparse.ArgumentParser(description='Reads data from Arduino and streams to CouchDB with option of realtime graphing using Plotly')
parser.add_argument('-f','--serialfile', help='Serial connection file handle to Arduino',required=False, default='/dev/ttyACM0')
parser.add_argument('-r','--rate', help='Rate in seconds to save sensor data to CouchDB',required=False, default=60, type=int)
parser.add_argument('-nc','--no-couchdb', help='Prevents sending of data to CouchDB',required=False)
parser.add_argument('-g','--graph', help='Graphs data to Plotly',required=False)
parser.add_argument('-u','--username', help='Plot.ly username',required=False)
parser.add_argument('-k','--apikey', help='Plot.ly API Key',required=False)
parser.add_argument('-t','--token', help='Plot.ly Stream Key',required=False)
parser.add_argument('-gr','--graph-rate', help='Plot.ly Streaming Rate',required=False, default=.125, type=int)
args = parser.parse_args()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

SERIAL_HANDLE=args.serialfile
RATE=9600

logging.info("Opening connection to %s at rate of %i", SERIAL_HANDLE, RATE)
ser = serial.Serial(SERIAL_HANDLE, RATE)

if not args.no_couchdb:
    couch = couchdb.Server()
    readings = couch['readings']

if args.graph:
    logging.info("Graphing to Plot.ly")
    username = 'mhossein2015'
    api_key = 'xe1j0wicu4'
    stream_token1 = 'motco7q58q'
    stream_token2 = '96jh1bgy95'
    stream_token3 = 'pn0gxn5x0e'

    py.sign_in(username, api_key)

    powertrace = Scatter(
        x=[],
        y=[],
        stream=dict(
            token=stream_token1,
            maxpoints=200
        )
    )

    currenttrace = Scatter(
        x=[],
        y=[],
        stream=dict(
            token=stream_token2,
            maxpoints=200
        )
    )

    powerlayout = Layout(
        title='Power Generation from Solar Panel',
        yaxis=YAxis(
            title='Power (W)'
        )
    )

    currentlayout = Layout(
        title='Temperature Readings',
        yaxis=YAxis(
            title='Temperature (C)'
        )
    )

    fig1 = Figure(data=[powertrace], layout=powerlayout)
    print py.plot(fig1, filename='Raspberry Pi Streaming Power Information')
    stream1 = py.Stream(stream_token1)
    stream1.open()
    fig2 = Figure(data=[currenttrace], layout=currentlayout)
    print py.plot(fig2, filename='Raspberry Pi Streaming Temperature Information')
    stream2 = py.Stream(stream_token2)
    stream2.open()

# There is a constant stream of data coming from the Arduino. The first time
# reading may be in the middle of the stream, which would not be a valid
# json string. We'll read the first n to create a stready-state reading.
for i in range(5):
    ser.readline()

last_save = 0
last_plot = 0

logging.info("Saving to CouchDB every %i seconds", args.rate)
ser = serial.Serial(SERIAL_HANDLE, RATE)

while True:
    raw = ser.readline()
    logging.debug("Raw reading: %s", raw)

    data = json.loads(raw)
    data['time'] = time.time()

    logging.debug("JSON reading: %s", data)

    if not args.no_couchdb:
        if time.time() - last_save > args.rate:
            readings.save(data)
            last_save = time.time()

    if args.graph and time.time() - last_plot > args.graph_rate:
        stream1.write({'x': datetime.datetime.now(), 'y': data['power']})
        stream2.write({'x': datetime.datetime.now(), 'y': data['temperature']})
        last_plot = time.time()
