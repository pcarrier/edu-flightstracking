#!/usr/bin/env python
import sys
sys.path.append("webpy/")
import web
from flighttracking.flight import *

flightsXML = open("../xml/examples/flights1.xml","r").read()
flights = FlightsTracking(flightsXML)

urls = (
    '/', 'main',
    '/flights.xml', 'flights',
    '/flights.kml', 'kml'
    )

app = web.application(urls, globals())

class main:
    def GET(self):
        web.redirect('/static/main.html')

class flights:
    def GET(self):
        return flights.tostring()
    def POST(self):
        pass
    
class kml:
    def GET(self):
        return flights.tokml()

if __name__ == "__main__":
    app.run()
