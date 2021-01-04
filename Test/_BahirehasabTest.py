import sys
lst = sys.path[0].split("/")
string = ""
for i in range(len(lst)-1):
    string += lst[i] + "/" 
sys.path.append(string)

from Calendar import Bahirehasab
import unittest

class BahirehasabTest(unittest.TestCase):
    bh = Bahirehasab.Bahirehasab(2012)
    
    def metkih(self):
        self.assertEqual(BahirehasabTest.bh.metkih, 24)
    
    def abekete(self):
        self.assertEqual(BahirehasabTest.bh.abekte, 6)
    
    def newewe(self):
        self.assertEqual(BahirehasabTest.bh.getNewewe()["month"], "የካቲት")
        self.assertEqual(BahirehasabTest.bh.getNewewe()["date"], "2")
    
    def getSingleBealorTsom(self): 
        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ዓቢይ ጾም")["month"], "የካቲት")
        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ዓቢይ ጾም")["date"], "16")
        
        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ደብረ ዘይት")["month"], "መጋቢት")
        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ደብረ ዘይት")["date"], "13");

        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ሆሣዕና")["month"], "ሚያዝያ")
        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ሆሣዕና")["date"], "4");

        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ስቅለት")["month"], "ሚያዝያ")
        self.assertEqual(BahirehasabTest.bh.getSingleBealOrTsom("ስቅለት")["date"], "9");

        
bh_test = BahirehasabTest()
bh_test.metkih()
bh_test.abekete()
bh_test.newewe()
bh_test.getSingleBealorTsom()