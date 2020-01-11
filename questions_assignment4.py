class MyDate(object):
   
    def __init__(self,userDay='',userMonth='',userYear='2020'):
        self.day=userDay
        self.month=userMonth
        self.year=userYear

    def __repr__(self):
        return{'day':self.day,'month':self.month,'year':self.year}
    

    def __str__(self):
        return str(self.day)+'.'+str(self.month)+'.'+str(self.year)

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year
    
    def setDay(self,dayValue):
        if (dayValue>=1 and dayValue<=30):
            self.day=dayValue
        else:
          self.day=''

    def setMonth(self,monthValue):
        if(monthValue>=1 and monthValue<=12):
            self.month=monthValue
        else:
          self.month=''

    def setYear(self,yearValue):
        if(yearValue>=1900 and yearValue<=2100):
            self.year=yearValue
        else:
          self.year=''

    def dispatch(msg):
        if msg=='getDay':
            return getDay
        elif msg=='getMonth':
            return getMonth
        elif msg=='getYear':
            return getYear
        elif msg=='setDay':
            return setDay
        elif msg=='setMonth':
            return setMonth
        elif msg=='setYear':
            return setYear


date=MyDate()
print(date)
date.setDay(31)
date.setDay(11)
date.setMonth(12)
date.setYear(2021)
print(date)
