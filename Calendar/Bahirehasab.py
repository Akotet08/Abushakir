# -*- coding: utf-8 -*-
import sys
lst = sys.path[0].split("/")
string = ""
for i in range(len(lst)-1):
    string += lst[i] + "/" 
sys.path.append(string)

from Util import Util as util
from Util import Constants as constants
from datetime import datetime, timezone 
import pytz
from Calendar import etDateTime
from Util import Calander_Exceptions as exception

class Bahirehasab:  
    def __init__(self, year = None):
        if year == None:
            localtime = datetime.now(timezone.utc).astimezone(pytz.timezone("Africa/Addis_Ababa"))
            lst_now = etDateTime.EtDateTime()._parse(str(localtime))
            year, month, day = lst_now[0], lst_now[1], lst_now[2]
            Ethiopia_day = util.Util().gregorianToEthiopic(year, month, day)
            self.__year = Ethiopia_day[0]
        else:
            self.__year = year
        self.ameteAlem = 5500 + self.__year
        self.rabeet = self.ameteAlem // 4
        self.wenber = util.Util().getWenber(5500, self.__year)
        self.abekte = self.wenber * 11 % 30
        if self.wenber == 0:
            self.metkih = 30
        else:
            self.metkih = self.wenber * 19 % 30
            
    def getEvange(self, boolean = False):
        result = self.ameteAlem % 4
        if boolean:
            return constants.Constants().evangelists[result]
        else:
            return str(result)
    
    def getMesekerem1(self, boolean = False):
        result = int((self.__year + constants.Constants().ameteFida + self.rabeet) % 7)
        if boolean:
            return constants.Constants().weekdays[result]
        else:
            return str(result)
        
    def getYear(self):
        return self.__year
    
    def getYebealMitkehWer(self):
        if self.metkih > 14:
            return 1
        return 2
    
    # Returns the date Tsome newewe will be at. 
    
    def getNewewe(self):
        meskerem1 = self.getMesekerem1(True)
        month = self.getYebealMitkehWer()
        day_tewsak = 0
        for i in util.Util().getyeeletTewsak().keys():
            if i == constants.Constants().weekdays[(util.Util().indexOf(meskerem1, constants.Constants().weekdays) + self.metkih - 1) % 7]:
                day_tewsak = util.Util().getyeeletTewsak()[i]
        monthName = ""
        if day_tewsak + self.metkih > 30:
            monthName = "የካቲት"
        else:
            monthName = "ጥር"     
        
        if month == 2:
            monthName = "የካቲት"
            tikimt1 = constants.Constants().weekdays[(util.Util().indexOf(meskerem1, constants.Constants().weekdays) + 2) % 7]
            metkihElet = constants.Constants().weekdays[(util.Util().indexOf(tikimt1, constants.Constants().weekdays) + self.metkih - 1) % 7]
            for i in util.Util().getyeeletTewsak().keys():
                if i == constants.Constants().weekdays[(util.Util().indexOf(metkihElet, constants.Constants().weekdays) + self.metkih - 1)%7]:
                    day_tewsak = util.Util().getyeeletTewsak()[i]
                    
        date = self.metkih + day_tewsak
        value = [monthName]
        if date % 30 == 0:
            value.append(str(30))
        else:
            value.append(str(date % 30))
            
        return util.Util().getNeweweDate(value)
    
    ''' Returns HashMap object which contains beal name,month and date.
       Example : {beal: ትንሳኤ, day: {month: ሚያዝያ, date: 20}}
     '''
     
    def getAllAtswamat(self, beal, numOfDays):
        mebjaHamer = self.getNewewe()
        all = {}
        h2 = {}
        h2["month"] = constants.Constants().months[util.Util().indexOf(mebjaHamer["month"], constants.Constants().months)  + (numOfDays // 30)]
        values = [beal, h2]
        if (int(mebjaHamer["date"]) + numOfDays) % 30 == 0:                
            h2["date"] = "30"
        else:
            h2["date"] = str((int(mebjaHamer["date"]) + numOfDays) % 30)
            
        all = util.Util().getAllAtswamatwDate(values)
        
        return all
    
    
    #Returns if a holiday is movable or not

    def isMovableHoliday(self, name):
        if name in constants.Constants().yebealTewsak:
            return True
        return False
    
    '''Returns the month and the day of given feast of the fasting or feasting (Holiday) in the form of HashMap.
       Example.Example : {month: ሚያዝያ, date: 20}
    '''

    def getSingleBealOrTsom(self, name):
        status = self.isMovableHoliday(name)
        if status:
            mebajaHamer = self.getNewewe()
            tewsak = int(constants.Constants().yebealTewsak[name])
            values = [constants.Constants().months[(util.Util().indexOf(mebajaHamer["month"], constants.Constants().months) + (int(mebajaHamer["date"]) + tewsak) // 30)], str((int(mebajaHamer["date"]) + tewsak) % 30)]
        else:
            raise exception.BealNameException ("Holiday is not a movable one. Please provide holidays between ነነዌ and ጾመ ድህነት")
        
        return util.Util().getSingleBealOrTsomDate(values)
    
