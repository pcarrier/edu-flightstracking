# -*- coding: utf-8 -*-
import lxml
from lxml import etree
import re
from lxml.etree import Element, tostring

class Location():
    __node__=None
    __airport__=None
    def __init__(self, node):
        self.__node__=node
        try:
            airports = self.__node__.xpath("./f:airport",namespaces={"f":self.__node__.nsmap[None]})
        except:
            airports = self.__node__.xpath("./airport")
        if(len(airports)!=1):
            raise Exception, "Aucun noeud airport trouvé"
        else:
            self.__airport__=airports[0]
    def setCoordinates(self, lat, long, z):
        E=Element("coordinates")
        E.text="%s, %s, %s"%(lat, long, z)
        self.__node__.append(E)
        
    def __str__(self):
        return self.__getPrettyName__()
    def __getPrettyName__(self):
             return "%s, %s, %s"% (self.__airport__.get("name"), self.__airport__.get("city"),  self.__airport__.get("country"))  


class FlightsTracking():
    __node__=None
    ___flights___ = []
    ___locations___ = []
    __nodename__ = "flightsTracking"
    def __init__(self, node):
            self.__node__=node
            try:
                flightsXp = "//f:flights/f:flight"
                locationsXp = "//f:locations/f:location"
                
                flightsNode = node.getroot().xpath(flightsXp,namespaces={"f":node.getroot().nsmap[None]})
                locationsNode = node.getroot().xpath(locationsXp,namespaces={"f":node.getroot().nsmap[None]})
            except:
                flightsXp = "//flights/flight"
                locationsXp = "//locations/location"
                
                flightsNode = node.xpath(flightsXp)
                locationsNode = node.xpath(locationsXp)
            for fnode in flightsNode:
                self.___flights___.insert(- 1, fnode)            
            for lnode in locationsNode:
                self.___locations___.insert(- 1,Location(lnode))
    def getNode(self):
        return self.__node__
    def __getitem__(self,attr):
        return getattr(self, "___%s___"%attr)
    def tostring(self):
        return tostring(self.__node__)