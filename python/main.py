#!/usr/bin/env python
import sys
sys.path.append("webpy/")
import web
from flighttracking.flight import *

flightsXML = open("../xml/examples/flights1.xml","r").read()
flights = FlightsTracking.fromstring(flightsXML)
geoflights = FlightsTracking.fromstring(flightsXML).geocode()

urls = (
    '/', 'main',
    '/flights.xml', 'native',
    '/geoflights.xml', 'geonative',
    '/flights.kml', 'kml'
    )

app = web.application(urls, globals())

class main:
    def GET(self):
        web.redirect('/static/main.html')

class native:
    def GET(self):
        return flights.tostring()
    def POST(self):
        print web.input()
        flights = FlightsTracking.fromstring(flightsXML)
        geoflights = FlightsTracking.fromstring(flightsXML).geocode()
        return "OK"

class geonative:
    def GET(self):
        return geoflights.tostring()
    
class kml:
    def GET(self):
        return geoflights.tokml()

if __name__ == "__main__":
    app.run()
