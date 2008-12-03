from lxml import etree
import unittest
import sys
#I want to be able to use my modules... 
sys.path.append("../")
from flighttracking.flight import *


class FlightTest(unittest.TestCase):
    pass

def test_suite():
    tests=[unittest.makeSuite(FlightTest)]
    return unittest.TestSuite(tests)

if __name__=="__main__":
    unittest.main(defaultTest="test_suite")
