import Converter
import unittest

class ConverterTest(unittest.TestCase):
    convert = Converter.Converter()
    
    def convert_1_10_ToGeez(self):
        self.assertEqual(ConverterTest.convert.convert_1_10_ToGeez(4), "፬")
    
    def convert_11_100_ToGeez(self):
        self.assertEqual(ConverterTest.convert.convert_11_100_ToGeez(15), "፲፭")
    
    def convert_101_1000_ToGeez(self):
        self.assertEqual(ConverterTest.convert.convert_101_1000_ToGeez(105), "፩፻፭")
    
    def convertToEthiopic(self):
        self.assertEqual(ConverterTest.convert.convertToGeez(2013), "፳፻፲፫")
    
    
c = ConverterTest()
c.convert_1_10_ToGeez()
c.convert_11_100_ToGeez()
c.convert_101_1000_ToGeez()
c.convertToEthiopic()