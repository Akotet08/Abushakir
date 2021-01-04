# Abushakir (ባሕረ ሃሳብ)

The words Bahire Hasab originate from the ancient language of Ge'ez, ( Arabic: Abu Shakir) is a
time-tracking method, devised by the 12th pope of Alexandria, Pope St. Dimitri.

## What does it mean?

"Bahire Hasab /'bəhrɛ həsəb'/  " simply means "An age with a descriptive and chronological number". In some books it can also be found as "Hasabe Bahir", in a sense giving time an analogy, resembling a sea.

This package allows developers to implement Ethiopian Calendar and Datetime System in their application(s)`.

This package is implemented using the [UNIX EPOCH](https://en.wikipedia.org/wiki/Unix_time) which
means it's not a conversion of any other calendar system into Ethiopian, for instance, Gregorian Calendar.

Unix Epoch is measured using milliseconds since 01 Jan, 1970 UTC. In unix epoch leap seconds are ignored.


## Getting started


In your library add the following import:

```python 
from abushakir import *
```
## Example

''' python 


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
         

'''



## Contributors

Thanks to the following people who have contributed to this project:

* [@Akotet08](https://github.com/Akotet08) 📖


<!---You might want to consider using something like the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).--->

## Contact

If you want to contact me you can reach me at <akiyeshaw@gmail.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
