# -*- coding: utf-8 -*-

import sys
sys.path.append("./abushakir/util")


import Calander_Exceptions
import Bahirehasab
import ETC 
import etDateTime

class Example:
    def main(self):
        
        '''
        etDateTime Module [etDateTime]
        ''' 
        # now = etDateTime.EtDateTime()
        # now = now.now()
        # print (now.getDate())
        # print (now.getYear(), now.getMonth(), now.getDay())
        # print (now.getHour(), now.getMinute(), now.getSecond())
        
        # covidFirstConfirmed = etDateTime.EtDateTime(2012,  7,  4)
        # covidFirstConfirmedEpoch = covidFirstConfirmed.fromMillisecondsSinceEpoch(covidFirstConfirmed.moment)
        # print (covidFirstConfirmedEpoch.getDate())
        
        # covidFirstDeath = covidFirstConfirmed.parse("2012-07-26 23:00:00");
        # print(covidFirstDeath.to_String())
        # print(covidFirstDeath.isBefore(covidFirstConfirmed))
        # print(covidFirstDeath.isAfter(covidFirstConfirmed))
        # print(covidFirstDeath.compareTo(covidFirstConfirmed))
        
        
        ''' 
         Ethiopian Calendar Module [ETC]
         '''
        
        # ethiopian_calander = ETC.ETC(2011, 10, 1)
        # print(ethiopian_calander.monthDays())
        # print(ethiopian_calander.monthDays(True, True))
        
        # print(ethiopian_calander.nextMonth().getMonth())  
        # print(ethiopian_calander.previousYear().getYear())
       
        ''' 
         Bahirehasab Module [Bahirehasab]
         '''
        # bh = Bahirehasab.Bahirehasab()
        # print (bh.getSingleBealOrTsom("ትንሳኤ"))
        # print (bh.getAllAtswamat("ትንሳኤ", 69))
        # print (bh.getEvange())
        
        


if __name__ == "__main__":
    obj = Example()
    obj.main()


