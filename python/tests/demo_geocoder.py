# -*- coding: utf-8 -*-
#!/usr/bin/env python

import lxml
from lxml import etree
import unittest
import sys, os

#I want to be able to use my modules...s
sys.path.append("../")
#print "demo_geocoder path :",os.path.abspath(os.path.curdir)
from flighttracking.flight import *
from service import google

def loadFile(xmlString):
    T =FlightsTracking.fromstring(xmlString)
    return T

def save(doc, file_out):
    f=open(file_out,"w")
    f.write(doc.tostring())
    f.close()
def usage():
    print "usage : \n%s file_in file_out"%sys.argv[0]
if __name__=="__main__":
    if len(sys.argv)==3:
        file_in=sys.argv[1]
        file_out=sys.argv[2]
        f=open(file_in)
        doc=loadFile(f.read())
        a=doc.geocode()
        #print a.tostring()
        #print doc.tostring()
        save(doc, file_out)
        print doc.tokml()
    else:
        usage()