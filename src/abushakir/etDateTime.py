# -*- coding: utf-8 -*-

import Util as util
import Constants as constants
from datetime import datetime, timezone 
import pytz

class EtDateTime: 
    '''
    etDateTime can represent time values that are at a distance of at most
     * 100,000,000 days from epoch (1970-01-01): -271821-04-20 to 275760-09-13.
     *
     * Create a etDateTime object by using one of the constructors
     * or by parsing a correctly formatted string,
     * which complies with a subset of ISO 8601.
     * Note that hours are specified between 0 and 23,
     * as in a 24-hour clock.
     * For example:
     *
     * now = EtDateTime().now
     * covid19Confirmed = EtDateTime(2012, 7, 4)
     * lockdownBegin = EtDateTime().fromMillisecondsSinceEpoch(1586215439441)
     * ```
     *
     * Once created, the value of an etDateTime object may not be changed.
     *
     * You can use properties to get
     * the individual units of an EtDatetime object.
     *
     * ```
     *  covid19Confirmed.year == 2012;
     *  covid19Confirmed.month == 7;
     *  covid19Confirmed.day == 2;
     * ```
     *
     * For convenience and readability,
     * the etDateTime class provides a constant for each day and month
     * name - for example, መስከረም and ማግሰኞ.
     * You can use these constants to improve code readability:
     *
     *
     * Day and month indexes begin at 0, and the week starts on Monday (ሰኞ).
     * That is, the constants መስከረም and ሰኞ are both 1.
     *
     * ## Comparing etDateTime objects
     *
     * The etDateTime class contains several handy methods,
     * such as isAfter, isBefore, and isAtSameMomentAs,
     * for comparing etDateTime objects.
     *
     * ```
     *  lockdownBegin.isAfter(covid19Confirmed);
     *  covid19Confirmed.isBefore(lockdownBegin);
    '''
    def __init__(self, year = None, month = 1, day = 1, hour = 0, minute = 0, second = 0, millisecond = 0):
        if year == None:
            localtime = str(datetime.now(timezone.utc).astimezone(pytz.timezone("Africa/Addis_Ababa")))
            lst_now = self._parse(str(localtime))
            year, month, day = lst_now[0], lst_now[1], lst_now[2]
            Ethiopia_day = util.Util().gregorianToEthiopic(year, month, day)
            self.__year = Ethiopia_day[0]
        else:
            self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__millisecond = millisecond
        self.__monthGeez = constants.Constants().months[self.__month -1]
        self.__dayGeez = constants.Constants().dayNumbers[self.__day -1]
        self.fixed = self.fixedFromEthiopic(year, month, day)
        self.moment = self._dateToEpoch(year, month, day, hour, minute, second, millisecond)
        
    def getYear(self):
        return self.__year
    
    def getMonth(self):
        return self.__month
    
    def getDay(self):
        return self.__day
    
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def getMillisecond(self):
        return self.__millisecond
    
    def getDayGeez(self):
        return self.__dayGeez
    
    def getMonthGeez(self):
        return self.__monthGeez
    
    def fixedFromEthiopic(self, year, month, day):
        return (constants.Constants().ethiopicEpoch - 1) + (365 * (year - 1) )+ (year / 4) + (30 * (month - 1)) + day
    
    def now(self):
        localtime = str(datetime.now(timezone.utc).astimezone(pytz.timezone("Africa/Addis_Ababa")))
        lst_now = self._parse(localtime)
        year = lst_now[0]
        month = lst_now[1]
        day = lst_now[2]
        hour = lst_now[3]
        minute = lst_now[4]
        second = lst_now[5]
        millisecond = lst_now[6]
        res = util.Util().gregorianToEthiopic(year, month, day)
        
        return EtDateTime(res[0], res[1], res[2], hour, minute, second, millisecond)
        
    def _parse(self, string):
        lst_now = [0]* 7
        lst_now[0] = int(string[0:4])
        lst_now[1] = int(string[5:7])
        lst_now[2] = int(string[8:10])
        
        if int(string[11:13]) > 12:
            lst_now[3] = self.__EthiopianHour(int(string[11:13]) -12 )
        else: 
            lst_now[3] = self.__EthiopianHour(int(string[11:13]))
            
        lst_now[4] = int(string[14:16])
        lst_now[5] = int(string[17:19])
        lst_now[6] = int(string[21:].split("+")[0])

        return lst_now
    
    def parse(self, string):
        lst_now = [0]* 7
        lst_now[0] = int(string[0:4])
        lst_now[1] = int(string[5:7])
        lst_now[2] = int(string[8:10])
        
        if int(string[11:13]) > 12:
            lst_now[3] = self.__EthiopianHour(int(string[11:13]) -12 )
        else: 
            lst_now[3] = self.__EthiopianHour(int(string[11:13]))
            
        lst_now[4] = int(string[14:16])
        lst_now[5] = int(string[17:19])
        
        if len(string) > 19:
            lst_now[6] = int(string[20:])
        else:
            lst_now[6] = 0
        
        return EtDateTime(lst_now[0], lst_now[1], lst_now[2], lst_now[3], lst_now[4], lst_now[5], lst_now[6])
    
    def __EthiopianHour(self, gregorianHour):
        if gregorianHour + 6 > 12:
            return gregorianHour + 6 -12
        return gregorianHour + 6
    
    def getDate(self):
        keys = ["year","month","day"]
        values = [self.__year, self.__month, self.__day]
        a = {keys[i]: values[i] for i in range(len(keys))}
        return a
    
    def yearFirstDay(self):
        rabeet = (self.__year + constants.Constants().ameteFida) // 4
        return (constants.Constants().ameteFida + rabeet) % 7
    
    def getWeekday(self):
        firstDay = self.yearFirstDay()
        return (firstDay + ((self.__month - 1) * 2)) % 7
    
    def isLeapYear(self):
        if self.__year % 4 == 3:
            return True
        return False
    
    def _dateToEpoch(self, year, month, date, hour, minute, second, millisecond):
        constant = constants.Constants()
        return ((self.fixedFromEthiopic(year, month, date) - constant.unixEpoch) * constant.dayMilliSec) + (hour * constant.hourMilliSec) + (minute * constant.minMilliSec) + (second * constant.secMilliSec) +  millisecond
    
    def fixedFromUnix(self, ms):
        return (constants.Constants().unixEpoch + int(ms/ 86400000))
    
    def to_String(self):
        ut = util.Util()
        y = ut._fourDigits(self.__year);
        m = ut._twoDigits(self.__month);
        d = ut._twoDigits(self.__day);
        h = ut._twoDigits(self.__hour);
        min = ut._twoDigits(self.__minute);
        sec = ut._twoDigits(self.__second);
        ms = ut._threeDigits(self.__millisecond);
        return y + "-" + m + "-" + d + " " + h + ":" + min + ":"+ sec + "." + ms;
    
    # Returns true if current instance occurs before the other instance

    def isBefore(self, other):
        return self.fixed < other.fixed and self.moment < other.moment
    

    # Returns true if current instance occurs after the other instance
 
    def isAfter(self, other):
        return self.fixed > other.fixed and self.moment > other.moment
    

    # Returns true if current instance occurs at the same time as the other instance 

    def isAtSameMomentAs(self, other):
        return self.fixed == other.fixed and self.moment == other.moment
    
    def compareTo(self, other):
        if (self.isBefore(other)):
            return -1;
        elif (self.isAtSameMomentAs(other)):
            return 0;
        else:
            return 1;
    
    def fromMillisecondsSinceEpoch(self,millisecondsSinceEpoch):
        moment = millisecondsSinceEpoch
        fixed = self.fixedFromUnix(moment)
        return self.withValue(fixed,moment) 

    def withValue(self, fixed, moment):
        constant = constants.Constants()
        year = (4 * (fixed - constant.ethiopicEpoch) + 1463) // 1461
        month = int(((fixed - self.fixedFromEthiopic(year, 1, 1)) // 30) + 1)
        day = int(fixed + 1 - self.fixedFromEthiopic(year, month, 1))
        hour = int((moment / constant.hourMilliSec) % 24)
        minute = int((moment / constant.minMilliSec) % 60)
        second = int((moment / constant.secMilliSec) % 60)
        millisecond = int((float(moment) % 1000))
        
        return EtDateTime(year,month,day,hour,minute,second,millisecond)
    


