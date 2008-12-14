# -*- coding: utf-8 -*-
import lxml
from lxml import etree
import re
from lxml.etree import Element, tostring
import os, sys, copy

sys.path.append("../")
from settings import FlightNS, xsltfile
from service import google

class Location(object):
    __node__ = None
    __airport__ = None
    
    def __init__(self, node):
        self.__node__ = node
        airports = self.__node__.xpath("./f:airport", namespaces={"f":FlightNS})

        if(len(airports) != 1):
            print "hop", len(airports)
            airport=self.__node__.find("./airport")
            if airport is not None: 
                self.__airport__ = airport
            else:
                raise Exception, "Aucun aéroport trouvé"
        else:
            self.__airport__ = airports[0]
    def setCoordinates(self, lat, long, z):
        coordinates = self.__node__.xpath("./f:coordinates", namespaces={"f":FlightNS})
        if len(coordinates) == 0:
            E = Element("coordinates")
            E.text = "%s, %s, %s" % (lat, long, z)
            self.__node__.append(E)
        elif len(coordinates) == 1:
            coordinates[0].text = "%s, %s, %s" % (lat, long, z)
        else:
            raise Exception, "Multiple coordonnées pour un point"
    def setName(self, name):
        self.__node__.set("name", name)
    def setAirportCode(self, code):
        self.__airport__.set("code", code)
    def setAirportName(self, name):
        self.__airport__.set("name", name)
    def setAirportCity(self, city):
        self.__airport__.set("name", city)
    def setAirportCountry(self, country):
        self.__airport__.set("name", country)
    def setAirportGate(self, gate):
        gates = self.__node__.xpath("./f:gate", namespaces={"f":FlightNS})
        if len(gates) == 0:
            E = Element("gate")
            E.set('name', gate)
            self.__node__.append(E)
        elif len(gates) == 1:
            gates[0].set('name', gate)
        else:
            raise Exception, "Plusieurs portes trouvées"
    def getNode(self):
        return self.__node__
    def getName(self):
        return self.__node__.get("name")
    def getAirportCode(self):
        return self.__airport__.get("code")
    def getAirportName(self):
        return self.__airport__.get("name")
    def getAirportCity(self):
        return self.__airport__.get("name")
    def getAirportCountry(self):
        return self.__airport__.get("name")
    def getAirportGate(self, gate):
        gates = self.__node__.xpath("./f:gate", namespaces={"f":FlightNS})
        if len(gates) == 0:
            return None
        elif len(gates) == 1:
            return gates[0].get('name')
        else:
            raise Exception, "Plusieurs portes trouvées"
        
    def __str__(self):
        return self.__getPrettyName__()
    def __getPrettyName__(self):
             return "%s, %s, %s" % (self.__airport__.get("name"), self.__airport__.get("city"), self.__airport__.get("country"))  
    @classmethod
    def newWithData(self, name, airportName, airportCode, airportCity, airportCountry):
        loc = Element("location", attrib={"name":name},nsmap={"f":FlightNS})
        ap = Element("airport", attrib={"code":airportCode, "name":airportName, "country":airportCountry, "city":airportCity},
                     nsmap={"f":FlightNS})
        loc.append(ap)
        #print loc.xpath("./f:airport",namespaces={"f":FlightNS})
        print loc.find("./airport").tag
        a = Location(loc)
        a.setName(name)
        return a

class Flight():
    def __init__(self,node):
        self.__node__=node
        
        departures = self.__node__.xpath("./f:departure", namespaces={"f":FlightNS})
        arrivals = self.__node__.xpath("./f:arrival", namespaces={"f":FlightNS})
        
        if(len(departures) != 1):
            raise Exception, "Aucun départ trouvé"
        else:
            self.__departure__ = departures[0]
            
        if(len(arrivals) != 1):
            raise Exception, "Aucune arrivée trouvé"
        else:
            self.__arrivals__ = arrivals[0]
    def setName(self,name):
        self.__node__.set("name",name)
    def setStatus(self, status):
        self.__node__.set("status",status)
        
    def setDepDateTime(self, dateTime):
        self.__departure__.set("datetime",datetime)
    def setDepLoc(self, location):
        self.__departure__.set("location",location)
        
    def setArDateTime(self, dateTime):
        self.__arrival__.set("datetime",datetime)
    def setArLoc(self, location):
        self.__arrival__.set("location",location)
    
    def getName(self):
        return self.__node__.get("name")
    def getStatus(self, status):
        return self.__node__.get("status")
        
    def getDepDateTime(self, dateTime):
        return self.__departure__.get("datetime")
    def getDepLoc(self, location):
        return self.__departure__.get("location")
        
    def getArDateTime(self, dateTime):
        return self.__arrival__.get("datetime")
    def getArLoc(self, location):
        return self.__arrival__.get("location")
    def getNode(self):
        return self.__node__
    @classmethod
    def newWithData(self, name, status, depDatetime, depLoc, arDatetime, arLoc):
        fl = Element("flight", attrib={"name":name,"status":status}, nsmap={None:FlightNS, "f":FlightNS})
        dep = Element("departure", attrib={"code":airportCode, "name":airportName},nsmap={None:FlightNS, "f":FlightNS})
        ar = Element("arrival", attrib={"code":airportCode, "name":airportName},nsmap={None:FlightNS, "f":FlightNS})
        fl.append(dep)
        fl.append(ar)
        f = Flight(fl)
        return f
class Flights(list):
    def __init__(self, node):
        self.__node__ = node
        for fnode in self.__node__.getchildren():
            newFlight = Flight(fnode)
            self.append(newFlight)
    def getByName(self, name):
        for x in self:
            if x.getName() == name:
                return x
    def add(self, fl):
        self.append(fl)
        self.__node__.append(fl.getNode())
    def remove(self, flname):
        fl=self.getByName(flname)
        self.__node__.remove(fl.getNode())
        del fl
        
class Locations(list):
    def __init__(self, node):
        self.__node__ = node
        for fnode in self.__node__.getchildren():
            newLoc = Location(fnode)
            self.append(newLoc)
    def getByName(self, name):
        for x in self:
            if x.getName() == name:
                return x
    def add(self, loc):
        self.append(loc)
        self.__node__.append(loc.getNode())
    def remove(self, locname):
        loc=self.getByName(locname)
        self.__node__.remove(loc.getNode())
        del loc
        
class FlightsTracking(object):
    __node__ = None
    
    def __init__(self, node):
            self.__node__ = node
            flightsXp = "//f:flights"
            locationsXp = "//f:locations"

            self.flights = Flights(node.xpath(flightsXp, namespaces={"f":FlightNS})[0])
            self.locations = Locations(node.xpath(locationsXp, namespaces={"f":FlightNS})[0])

    def getNode(self):
        return self.__node__
    def __getitem__(self, attr):
        return getattr(self, "___%s___" % attr)
    def tostring(self):
        return tostring(self.__node__)
    
    def apply_xsl(self, xsl_file):
        if os.path.exists(xsl_file):
            xsl_doc = etree.parse(xsl_file)
            transform = etree.XSLT(xsl_doc)
            return etree.tostring(transform(self.__node__), pretty_print=True)
            #return etree.tostring(transform(self.__node__))
        else:
            raise Exception,"Le ficher %s n'existe pas."%xsl_file
    
    def geocode(self):
        doc=copy.deepcopy(self)
        for loc in doc.locations:
            lat, long,z=self._obtainLatLong(str(loc))
            if lat is not None and long is not None and z is not None:
                loc.setCoordinates(lat, long,z)
            else:
                raise Exception, "Can't obtains Coordinates"
        return doc
    def _obtainLatLong(self, place):
        rep=google.getResponse("Aéroport "+place)
        if rep is not None:
            try:
                root=etree.XML(rep)
            except:
                #File contains an utf-8 declaration but it's in fact iso-8859-1.....
                root=etree.XML(rep.replace("UTF-8","iso-8859-1"))
        coordinates=root.xpath("//g:coordinates",namespaces={"g":root.nsmap[None]})
        if len(coordinates)>0:
            lat, long, z= coordinates[0].text.split(',')
            return (lat, long, z)
        else:
            return (None, None, None) 
    def tokml(self):
        return self.apply_xsl(xsltfile)
    def tohtml(self):
        pass
    @classmethod
    def fromstring(cls, xmlString):
        xml_doc = etree.XML(xmlString)
        T = FlightsTracking(xml_doc)
        return T