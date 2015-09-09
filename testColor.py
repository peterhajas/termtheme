#!/usr/bin/python
import unittest
from color import Color

class TestColorMethods(unittest.TestCase):
    def _assertFloatsAreEqualEnough(self, f1, f2):
        diff = abs(f1 - f2)
        epsilon = 0.01
        self.assertTrue(diff < epsilon)
    def testThing(self):
        self.assertTrue(True)
    def testRGBStorage(self):
        color = Color(rgb=(0.1, 0.5, 0.9))
        self.assertTrue(color.r == 0.1)
        self.assertTrue(color.g == 0.5)
        self.assertTrue(color.b == 0.9)
    def testHSVConversion(self):
        color = Color(hsv=(0.5, 0.5, 0.5))
        self._assertFloatsAreEqualEnough(color.r, 0.5)
        self._assertFloatsAreEqualEnough(color.g, 0.25)
        self._assertFloatsAreEqualEnough(color.b, 0.25)
    def testShortCSSConversionWithHash(self):
        color = Color(hexStr='#F0E')
        self.assertTrue(color.r == 1.0)
        self.assertTrue(color.g == 0.0)
        self._assertFloatsAreEqualEnough(color.b, 0.933)
    def testShortCSSConversionWithoutHash(self):
        color = Color(hexStr='EF0')
        self._assertFloatsAreEqualEnough(color.r, 0.933)
        self.assertTrue(color.g == 1.0)
        self.assertTrue(color.b == 0.0)
    def testLongCSSConversionWithHash(self):
        color = Color(hexStr='#AABBCC')
        self._assertFloatsAreEqualEnough(color.r, 0.666)
        self._assertFloatsAreEqualEnough(color.g, 0.733)
        self._assertFloatsAreEqualEnough(color.b, 0.8)
    def testLongCSSConversionWithoutHash(self):
        color = Color(hexStr='DDEEFF')
        self._assertFloatsAreEqualEnough(color.r, 0.866)
        self._assertFloatsAreEqualEnough(color.g, 0.933)
        self._assertFloatsAreEqualEnough(color.b, 1.0)

if __name__ == '__main__':
    unittest.main()
