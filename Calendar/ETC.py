import sys
lst = sys.path[0].split("/")
string = ""
for i in range(len(lst)-1):
    string += lst[i] + "/" 
sys.path.append(string)

from Calendar import etDateTime as Et
from Util import Util as util
from Util import Constants as constants
from datetime import datetime, timezone 
import pytz

class  ETC:
    
    '''
     * The Ethiopian calendar is one of the the calendars which uses the solar
     * system to reckon years, months and days, even time. Ethiopian single year
     * consists of 365.25 days which will be 366 days with in 4 years period which
     * causes the leap year. Ethiopian calendar has 13  months from which 12 months
     * are full 30 days each and the 13th month will be 5 days or 6 days during
     * leap year.
     *
     *
     * Create [ETC] object instances which are days of certain month in a certain
     * year.
     *
     * ```
     * etc = ETC(2012, 7, 4)
     * ```
     *
     * or
     *
     * ```
     * today = ETC.today()
     * ```
     *
     * After creating instance of [ETC], you can navigate to the future or past
     * of the given date.
     *
     * ```
     * etc_nextMonth = today.nextMonth()
     * etc_prevMonth = today.prevMonth()
     * ```
     *
     * you can also get the same month of different year (the next year or
     * prev one)
     *
     * ```
     * etc_nextYear = today.nextYear()
     * etc_prevYear = today.prevYear()
     * ```
     *
     * All the available days within a single month can be found using
     *
     * ```
     * monthDaysIter = today.monthDays()
     * ```
     *
     * or just all of the days available in the given year can also be found using
     * ```
     * yearDaysIter = today.yearDays()
     * ```
     *
    '''
    
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.etDateTime = Et.EtDateTime(year, month, day)
    
    def getYear(self):
        return self.year
    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day
    
    def nextMonth(self):
        if self.month == 13:
            self.month = 1
            return ETC(self.year, self.month, self.day)
        return ETC(self.year, self.month + 1, self.day)

    def previousMonth(self):
        if self.month == 1:
            self.month = 13
            return ETC(self.year, self.month, self.day)
        return ETC(self.year, self.month - 1, self.day)
    
    def nextYear(self):
        return ETC(self.year + 1, self.month, self.day)
    def previousYear(self):
        return ETC(self.year - 1, self.month, self.day)
    
    def getGeezDay(self):
        return constants.Constants().dayNumbers[self.day - 1]
    
    @classmethod
    def today(cls):
        localtime = str(datetime.now(timezone.utc).astimezone(pytz.timezone("Africa/Addis_Ababa")))
        lst_now = Et.EtDateTime().parse(localtime)
        year = lst_now[0]
        month = lst_now[1]
        day = lst_now[2]
        hour = lst_now[3]
        minute = lst_now[4]
        second = lst_now[5]
        millisecond = lst_now[6]
        res = util.Util().gregorianToEthiopic(year, month, day)
        return ETC(res[0], res[1], res[2])
    
    def monthRange(self):
        result = [self.getWeekday()]
        if self.isLeapYear():
            result.append(6)
        else:
            result.append(5)
        return result
    
    def yearFirstDay(self):
        rabeet = (self.year + constants.Constants().ameteFida) // 4
        return (constants.Constants().ameteFida + rabeet) % 7
    
    def getWeekday(self):
        firstDay = self.yearFirstDay()
        return (firstDay + ((self.month - 1) * 2)) % 7
    
    def isLeapYear(self):
        if self.year % 4 == 3:
            return True
        return False
    
    def monthDays(self, geezDay = False, weekDayName = False):
        result = [0]* 4
        monthBeginning = self.monthRange()[0]
        daysInMonth = self.monthRange()[1]
        for i in range(daysInMonth):
            if (geezDay):
                result[0] = self.year
                result[1] = self.month
                result[2] = constants.Constants().dayNumbers[i]
                if weekDayName:
                    result[3] = constants.Constants().weekdays[monthBeginning]
                else:
                    result[3] = monthBeginning
                
            else:
                result[0] = self.year
                result[1] = self.month
                result[2] = i + 1
                if weekDayName:
                    result[3] = constants.Constants().weekdays[monthBeginning]
                else:
                    result[3] = monthBeginning
            
            monthBeginning = (monthBeginning + 1) % 7;
        
        return result;
    
    def _monthDays(self, geezDay = False, weekDayName = False):
        result = [0] * 4
        yr = Et.EtDateTime(self.year,self.month)
        monthBeginning = yr.getWeekday()
        if yr.getMonth() == 13:
            if yr.isLeap():
                daysInMonth = 6
            else:
                daysInMonth = 5
        else:
            daysInMonth = 30
        
        for i in range(daysInMonth):
            if (geezDay):
                result[0] = self.year
                result[1] = self.month
                result[2] = constants.Constants().dayNumbers[i]
                if weekDayName:
                    result[3] = constants.Constants().weekdays[monthBeginning]
                else:
                    result[3] = monthBeginning
                
            else:
                result[0] = self.year
                result[1] = self.month
                result[2] = i + 1
                if weekDayName:
                    result[3] = constants.Constants().weekdays[monthBeginning]
                else:
                    result[3] = monthBeginning
            
            monthBeginning = (monthBeginning + 1) % 7;
        
        return result;
    
    def yearDays (self, geezDay = False,  weekDayName = False):
        result = [0] * 4
        for i in range(len(constants.Constants().months)):
            result[0] = self.year
            result[1] = i + 1
            result[2] = geezDay
            result[3] = weekDayName
        return result
