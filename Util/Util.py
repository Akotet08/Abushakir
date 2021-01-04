# -*- coding: utf-8 -*-

import math

class Util:
    '''
     util class contains functions used to create HashMap objects, formatted Strings and to
     find the index of values from array.
     '''
     
    def __init__(self):
        self.JD_EPOCH_OFFSET_GREGORIAN = 1721426
        self.JD_EPOCH_OFFSET_AMETE_ALEM   = -285019
        self.JD_EPOCH_OFFSET_AMETE_MIHRET = 1723856
    
    def getyeeletTewsak(self):
        keys = ["አርብ","ሐሙስ","ረቡዕ","ማግሰኞ","ሰኞ","እሁድ","ቅዳሜ"]
        values = [2,3,4,5,6,7,8]
        yeeletTewsak = {keys[i]: values[i] for i in range(len(values))}
        
        return yeeletTewsak
    
    def getyebealTewsak(self):
        keys = ["ነነዌ","ዓቢይ ጾም","ደብረ ዘይት","ሆሣዕና","ስቅለት","ትንሳኤ","ርክበ ካህናት","ዕርገት","ጰራቅሊጦስ","ጾመ ሐዋርያት","ጾመ ድህነት"]
        values = [0,14,41,62,67,69,93,108,118,119,121]
        yebealTewsak = {keys[i]: values[i] for i in range(len(values))}
        
        return yebealTewsak
    
    def getAmeteAlem(self, year, ameteFeda):
        return year + ameteFeda
    
    def getWenber(self, ameteFeda, year):
        if ((year + ameteFeda) % 19 ) -1 < 0:
            return 0
        else:
            wenber = ((year + ameteFeda) % 19 ) -1
            return wenber
    def indexOf(self, string, lst):
        for i in range(len(lst)):
            if lst[i] == string:
                return i
        return -1
    
    def getNeweweDate(self, values):
        keys = ["month","date"]
        newew= {keys[i]: values[i] for i in range(len(keys))}
        return newew
         
    def getSingleBealOrTsomDate(self, values):
        keys = ["month","date"]
        singleBealOrTsom= {keys[i]: values[i] for i in range(len(keys))}
        return singleBealOrTsom
    
    def getAllAtswamatwDate(self, values):
        keys = ["beal","date"]
        allAtswamat = {keys[i]: values[i] for i in range(len(keys))}
        return allAtswamat
    
    def _fourDigits(self, n):
        absN = self.__abs(n)
        sign = ""
        if n < 0:
            sign = "-"
        if (absN >= 1000):
            return str(n)
        if (absN >= 100):
            return sign + "0" + str(absN)
        if (absN >= 10):
            return sign + "00" + str(absN)
        return sign + "000" + str(absN)
    
    def _sixDigits(self, n):
        absN = self.__abs(n)
        sign = ""
        if n < 0:
            sign = "-"
        if (absN >= 100000):
            return str(n)
        return sign + "0" + str(absN)
    
    def _threeDigits(self, n):
        if n >= 100:
            return str(n)
        if n >= 10:
            return "0" + str(n)
        return "00" + str(n)
         
    def _twoDigits(self, n):
        if n >= 10:
            return str(n)
        return "0" + str(n)
    
    def __abs(self, n):
        if n < 0:
            return -1 * n
        return n
    def getToJason(self, values):
        keys = ["year","month","date","hour","min","sec","ms"]
        toJason= {keys[i]: values[i] for i in range(len(keys))}
        return toJason
    
    def quotient(self, i,j):
        return int(math.floor(float(i) / j))
    
    def mod(self, i, j):
        return int(i - (j * self.quotient(i, j)))
    
    
    def gregorianToEthiopic(self, year, month, day):
        jdn = self.gregorianToJDN(year, month, day)

        return self.jdnToEthiopic( jdn, self.guessEraFromJDN( jdn ) )
    
    def guessEraFromJDN(self, jdn):
        if jdn >= self.JD_EPOCH_OFFSET_AMETE_MIHRET +365:
            return self.JD_EPOCH_OFFSET_AMETE_MIHRET
        else:
            return self.JD_EPOCH_OFFSET_AMETE_ALEM
    
    def jdnToEthiopic(self, jdn, era):
        r = self.mod((jdn - era), 1461)
        n = self.mod( r, 365 ) + 365 * self.quotient( r, 1460 ) 

        year = 4 * self.quotient( (jdn - era), 1461 )+ self.quotient( r, 365 )- self.quotient( r, 1460 )
        month = self.quotient( n, 30 ) + 1
        day   = self.mod( n, 30 ) + 1 

        return (year, month, day)
    
    def gregorianToJDN(self, year, month, day):
        s   = self.quotient ( year, 4 )- self.quotient ( year - 1, 4 )- self.quotient ( year, 100 )+ self.quotient ( year - 1, 100 )+ self.quotient ( year    , 400 )- self.quotient ( year - 1, 400 )
        t   = self.quotient ( 14 - month, 12 )
        
        n   = 31 * t * ( month - 1 )+ ( 1 - t ) * ( 59 + s + 30 * (month - 3) + self.quotient( (3*month - 7), 5) )+ day - 1
                
        j   = self.JD_EPOCH_OFFSET_GREGORIAN + 365 * (year - 1)+ self.quotient ( year - 1,   4 )- self.quotient ( year - 1, 100 ) + self.quotient ( year - 1, 400 ) + n
        
        return j
    
    def getgeezNumbers(self):
        keys = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,1000,10000]
        values = ["፩","፪", "፫", "፬", "፭", "፮", "፯", "፰", "፱", "፲", "፳", "፴", "፵","፶", "፷", "፸", "፹", "፺","፻", "፲፻", "፼"]
        geezNumbers = {keys[i] : values[i] for i in range(len(keys))}
        return geezNumbers
    
    


        


