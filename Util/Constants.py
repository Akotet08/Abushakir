# -*- coding: Utf-8 -*-

import sys
lst = sys.path[0].split("/")
string = ""
for i in range(len(lst)-1):
    string += lst[i] + "/" 
sys.path.append(string)

from Util import Util as ut

class Constants:
    def __init__(self):
        self.evangelists = ["ዮሐንስ", "ማቴዎስ", "ማርቆስ", "ሉቃስ"]
        self.ameteFida = 5500
        self.tinteAbekte = 11
        self.tinteMetkih = 19
        self.maxMillisecondsSinceEpoch = 8640000000000000.0
        self.ethiopicEpoch = 2796
        self.unixEpoch = 719163
        self.dayMilliSec = 86400000.0
        self.hourMilliSec = 3600000
        self.minMilliSec = 60000
        self.secMilliSec = 1000
        
        self.weekdays = ["ሰኞ","ማግሰኞ","ረቡዕ","ሐሙስ","አርብ","ቅዳሜ","እሁድ"]
        self.dayNumbers = ["፩","፪","፫","፬","፭","፮","፯","፰","፱","፲","፲፩","፲፪","፲፫","፲፬","፲፭","፲፮","፲፯","፲፰","፲፱","፳","፳፩","፳፪","፳፫","፳፬","፳፭","፳፮","፳፯","፳፰","፳፱","፴"]
        self.months = ["መስከረም","ጥቅምት","ኅዳር","ታኅሳስ","ጥር","የካቲት","መጋቢት","ሚያዝያ","ግንቦት","ሰኔ","ኃምሌ","ነሐሴ","ጷጉሜ"]

        util = ut.Util()
        
        self.yeeletTewsak = util.getyeeletTewsak()
        self.yebealTewsak = util.getyebealTewsak()
        self.geezNumbers = util.getgeezNumbers()

        

    
