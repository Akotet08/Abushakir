import etDateTime
import unittest

class etDateTimeTest(unittest.TestCase):
    ec = etDateTime.EtDateTime(2012, 7, 7)
    e = etDateTime.EtDateTime(2010)
    et = etDateTime.EtDateTime().parse("2012-07-07 15:12:17.500")
    etd = etDateTime.EtDateTime().now()
    ecc = etDateTime.EtDateTime().fromMillisecondsSinceEpoch(1585731446021)
    
    def getYear(self):
        self.assertEqual(2012,etDateTimeTest.ec.getYear())
        self.assertEqual(2010,etDateTimeTest.e.getYear())
        self.assertEqual(2012,etDateTimeTest.et.getYear())
        self.assertEqual(2012,etDateTimeTest.ecc.getYear())
        
    def getMonth(self):
        self.assertEqual(7,etDateTimeTest.ec.getMonth())
        self.assertEqual(1,etDateTimeTest.e.getMonth())
        self.assertEqual(7,etDateTimeTest.et.getMonth())
        self.assertEqual(7,etDateTimeTest.ecc.getMonth())

    def getDay(self):
        self.assertEqual(7,etDateTimeTest.ec.getDay())
        self.assertEqual(1,etDateTimeTest.e.getDay())
        self.assertEqual(7,etDateTimeTest.et.getDay())
        self.assertEqual(23,etDateTimeTest.ecc.getDay())
    
    def getDayGeez(self):
        self.assertEqual("፯",etDateTimeTest.ec.getDayGeez())
        self.assertEqual("፯",etDateTimeTest.et.getDayGeez())
        self.assertEqual("፳፫",etDateTimeTest.ecc.getDayGeez())
    
    def getMonthGeez(self):
        self.assertEqual("መጋቢት",etDateTimeTest.ec.getMonthGeez())
    

    def to_String(self):
        self.assertEqual("2012-07-07 09:12:17.500", etDateTimeTest.et.to_String())
        self.assertEqual("2012-07-23 08:57:26.021",etDateTimeTest.ecc.to_String())
        
    def getHour(self):
        self.assertEqual(9, etDateTimeTest.et.getHour())
        self.assertEqual(8, etDateTimeTest.ecc.getHour())

    def getMinute(self):
        self.assertEqual(12,etDateTimeTest.et.getMinute())
        self.assertEqual(57,etDateTimeTest.ecc.getMinute())
    

    def getSecond(self):
        self.assertEqual(17,etDateTimeTest.et.getSecond())
        self.assertEqual(26,etDateTimeTest.ecc.getSecond())
    

    def getMillisecond(self):
        self.assertEqual(500, etDateTimeTest.et.getMillisecond())
        self.assertEqual(21,etDateTimeTest.ecc.getMillisecond())
    
    def isAfter(self):
      self.assertTrue(etDateTimeTest.e.isAfter(etDateTime.EtDateTime(2001)))
    

    def isBefore(self):
        self.assertTrue(etDateTimeTest.ec.isBefore(etDateTime.EtDateTime(2020)))
    

    def isisAtSameMomentAs(self):
        self.assertTrue(etDateTimeTest.etd.isAtSameMomentAs(etDateTime.EtDateTime(etDateTimeTest.etd.getYear(),etDateTimeTest.etd.getMonth(),etDateTimeTest.etd.getDay(),etDateTimeTest.etd.getHour(),etDateTimeTest.etd.getMinute(),etDateTimeTest.etd.getSecond(),etDateTimeTest.etd.getMillisecond())))
  

        
        
et = etDateTimeTest()
et.getYear()
et.getMonth()
et.getDay()
et.getHour()
et.getMinute()
et.getSecond()
et.getMillisecond()
et.getDayGeez()
et.getMonthGeez()
et.to_String()
et.isAfter()
et.isBefore()
et.isisAtSameMomentAs()