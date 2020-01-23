#Patrick Lugassy 319266177
#Ivan Borisenco  317366102



#Question 1:

def make_instance(cls):
		"""Return a new object instance, which is a dispatch dictionary."""
		attributes = {}
		def get_value(name):
		    if name in attributes:
		        return attributes[name]
		    else:
		        value = cls['get'](name)
		        return bind_method(value, instance)
		def set_value(name, value):
		    attributes[name] = value
		instance = {'get': get_value, 'set': set_value}
		return instance

def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
            return value

def make_class(attributes, base_class=None):
    """Return a new class,which is a dispatch dictionary"""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name,value):
        attributes[name]=value
    def new(*args):
        return init_instance(cls,*args)
    cls={'get':get_value,'set':set_value,'new':new}
    return cls

def init_instance(cls,*args):
    """return a new object with type CLS,initialized with args"""
    instance=make_instance(cls)
    init=cls['get']('__init__')
    if init:
        init(instance,*args)
    return instance


def make_MyDate_class():
    def __init__(self, _day=0,_month=0,_year=2020):
        if _day >= 1 and _day <= 30:
            self['set']('day',_day)
        if _month >= 1 and _month <= 12:
            self['set']('month',_month)
        if _year >= 1900 and _year <=2100: 
            self['set']('year',_year)
    def setDay(self,_day=0):
        if _day >= 1 and _day <= 30:
            self['set']('day',_day)
    def setMonth(self,_month=0):
        if _month >= 1 and _month <= 12:
            self['set']('month',_month)
    def setYear(self,_year=2020):
        if _year >= 1900 and _year <=2100: 
            self['set']('year',_year)
    def getDay(self):
        return self['get']('_day')
    def getMonth(self):
        return self['get']('month')
    def getYear(self):
        return self['get']('year')        
    def __repr__(self):
        return f"myDate['new']({self['get']('day')},{self['get']('month')},{self['get']('year')})"
    
    def __str__(self):
        return str(self['get']('day'))+'.'+str(self['get']('month'))+'.'+str(self['get']('year'))


    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__,'setDay':setDay,'setMonth':setMonth,'setYear':setYear,'getDay':getDay,'getMonth':getMonth,'getYear':getYear})



def make_Person_class():
    def __init__(self,_FirstName,_LastName,_DOB,_ID):
        self['set']('FirstName',_FirstName)
        self['set']('LastName',_LastName)
        self['set']('DoB',_DOB)
        if _ID>0:
            self['set']('ID',_ID)
    def setFirstName(self,_FirstName):
        self['set']('FirstName',_FirstName)
    def setLastName(self,_LastName):
        self['set']('LastName',_LastName)
    def setDOB(self,_DOB):
        self['set']('DoB',_DOB)
    def setID(self,_ID):
        if _ID>0:
            self['set']('ID',_ID)
    def getFirstName(self):
        return self['get']('FirstName')
    def getLastName(self):
        return self['get']('LastName')
    def getDOB(self):
        return self['get']('DoB')
    def getID(self):
        return self['get']('ID')            
    def __repr__(self):
        return f"Person['new']('{self['get']('FirstName')}','{self['get']('LastName')}',{self['get']('DoB')['get']('__repr__')()},{self['get']('ID')})"

    def __str__(self):
        return ('Name:'+self['get']('FirstName')+' ' + self['get']('LastName') +'\n'
                'DoB:' + self['get']('DoB')['get']('__str__')() + '\n' 
                'ID:'+str(self['get']('ID')))
      
            
    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__,'setFirstName':setFirstName,'setLastName':setLastName,'setDOB':setDOB,'setID':setID,'getFirstName':getFirstName,'getLastName':getLastName,'getDOB':getDOB,'getID':getID})



def make_Student_class( ):

    def __init__(self,_FirstName,_LastName,_DOB,_ID,_Department,_Average,_Seniority):
        Person['get']('__init__',)(self,_FirstName,_LastName,_DOB,_ID)
        self['set']('Department',_Department)
        self['set']('Average',_Average)
        self['set']('Studying Seniority',_Seniority)
    def setDepartment(self,_Department):
        self['set']('Department',_Department)
    def setAverage(self,_Average):
        self['set']('Average',_Average)
    def setSSeniority(self,_Seniority):
        self['set']('Studying Seniority',_Seniority)
    def getDepartment(self):
        return self['get']('Department')
    def getAverage(self):
        return self['get']('Average')
    def getSSeniority(self):
        return self['get']('Studying Seniority')
    def __repr__(self):
        return f"Student['new']('{self['get']('FirstName')}','{self['get']('LastName')}',{self['get']('DoB')['get']('__repr__')()},{self['get']('ID')},'{self['get']('Department')}',{self['get']('Average')},{self['get']('Studying Seniority')})"

    def __str__(self):
         return (
                 (Person['get']('__str__')(self))+'\n'
                 'Learning:'+self['get']('Department')+'\n'
                 'Avg:' +str(self['get']('Average'))+'\n'
                 'Studying Seniority:'+str(self['get']('Studying Seniority'))
                 )

    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__,'setDepartment':setDepartment,'setAverage':setAverage,'setSSeniority':setSSeniority,'getDepartment':getDepartment,'getAverage':getAverage,'getSSeniority':getSSeniority},Person)


def make_Faculty_class():

    def __init__(self,_FirstName,_LastName,_DOB,_ID,_Teaching,_Salary,_Seniority):
        Person['get']('__init__',)(self,_FirstName,_LastName,_DOB,_ID)
        self['set']('Teaching',_Teaching)
        self['set']('Salary',_Salary)
        self['set']('Teaching Seniority',_Seniority)
    def setTeaching(self,_Teaching):
        self['set']('Teaching',_Teaching)
    def setSalary(self,_Salary):
        self['set']('Salary',_Salary)
    def setSeniority(self,_Seniority):
        self['set']('Teaching Seniority',_Seniority)
    def getTeaching(self):
        return self['get']('Teaching')
    def getSalary(self):
        return self['get']('Salary')
    def getSeniority(self):
        return self['get']('Seniority')
    def __repr__(self):
        return f"Faculty['new']('{self['get']('FirstName')}','{self['get']('LastName')}',{self['get']('DoB')['get']('__repr__')()},{self['get']('ID')},'{self['get']('Teaching')}',{self['get']('Salary')},{self['get']('Teaching Seniority')})"

    def attr(self):
        return ( 'Teaching:' + self['get']('Teaching')+ '\n'
                'Salary:' + str(self['get']('Salary'))+'\n'
                'Teaching Seniority:' + str(self['get']('Teaching Seniority')))

    def __str__(self):
        return ((Person['get']('__str__')(self))+'\n'
                'Teaching:' + self['get']('Teaching')+ '\n'
                'Salary:' + str(self['get']('Salary'))+'\n'
                'Teaching Seniority:' + str(self['get']('Teaching Seniority')))
   
    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__,'attr':attr},Person)



def make_TA_class():
    
    def __init__(self,_FirstName,_LastName,_DOB,_ID,_Department,_Average,_SSeniority,_Teaching,_Salary,_TSeniority):
        Student['get']('__init__')(self,_FirstName,_LastName,_DOB,_ID,_Department,_Average,_SSeniority)
        Faculty['get']('__init__')(self,_FirstName,_LastName,_DOB,_ID,_Teaching,_Salary,_TSeniority)
    
    def __repr__(self):
        return  f"TA['new']('{self['get']('FirstName')}','{self['get']('LastName')}',{self['get']('DoB')['get']('__repr__')()},{self['get']('ID')},'{self['get']('Department')}',{self['get']('Average')},{self['get']('Studying Seniority')},'{self['get']('Teaching')}',{self['get']('Salary')},{self['get']('Teaching Seniority')})"
      
    def __str__(self):
       return (
           Student['get']('__str__')(self) +'\n' +
           Faculty['get']('attr')(self)
       )
    
    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__},Student)



Date=make_MyDate_class()
Person=make_Person_class()
Student=make_Student_class()
Faculty=make_Faculty_class()
TA=make_TA_class()
myDate=Date['new'](12,6,1987)
myDate1=Date['new'](20,2,1980)
myDate2=Date['new'](30,12,1999)

Omri=Person['new']('Omri','Halabi',myDate,333333333)
Dani=Student['new']('Dani','israeli',myDate,312131145,'Software Engineering' ,85.3 ,4)
Yossi=Faculty['new']('Yossi','Levi',myDate1,123456789,'Science',18000,2)
Ben=TA['new']('Ben','Shvili',myDate2,987654312,'Chemistry',93,3,'Chemistry',6000,0.3)
#print(Ben['get']('__repr__')())
#print(Dani['get']('__str__')())
#print(Yossi['get']('__str__')())
#print(Ben['get']('__str__')())




#Question 2: 

from math import gcd

empty_rlist=None
def make_rlist(first, rest):
     """Make a recursive list from its first 	element and the rest."""
     if first==None:
        return empty_rlist
     return (first, rest)

def first(s):
 		"""Return the first element of a recursive 	list s."""
 		return s[0]
def rest(s):
 		"""Return the rest of the elements of a 	recursive list s."""
 		return s[1]

def len_rlist(s):
 		"""Return the length of recursive list s."""
 		length = 0
 		while s != empty_rlist:
 			s, length = rest(s), length + 1
 		return length

def getitem_rlist(s, i):
     """Return the element at index i of recursive list s."""
     while i > 0:
         s, i = rest(s), i - 1
     return first(s)



class Rational(object):
     def  __init__(self,number,denom):
         g=gcd(number,denom)
         self.number=number//g
         self.denom=denom//g
    
     def __repr__(self):
         return 'Rational({0},{1})'.format(self.number,self.denom)


def isRational(z):
     return type(z)==Rational

def isRlist(z):
     return type(z)==tuple

def isInt(z):
     return type(z)==int

def AppendRlist(rational,rlist):
     if  rest(rlist)==None:
         return make_rlist(first(rlist),make_rlist(rational,None))
     else:
         return make_rlist(first(rlist),AppendRlist(rational,rest(rlist)))


def MergeRlist(rlist1,rlist2):
     if len_rlist(rlist1)==0:
         return rlist2
     else:
         return make_rlist(first(rlist1),MergeRlist(rest(rlist1),rlist2))


def AddRational(rational1,rational2):
     nrational1,drational1=rational1.number,rational1.denom
     nrational2,drational2=rational2.number,rational2.denom
     return Rational(nrational1*drational2+nrational2*drational1,drational1*drational2)


def AddInt(int1,int2):
     return int1+int2


def SumIntRational(int1,rational2):
     nrational2,drational2=rational2.number,rational2.denom
     return Rational(int1*drational2+nrational2,drational2)



def MUltiplyRlist(n,l1):
       temp=l1
       temp2=()
       for i in range(n-1):
           temp2=MergeRlist(temp,l1)
           temp=temp2
           temp2=l1

       return temp


def MulRational(r1,r2):
      nr1,dr1=r1.number,r1.denom
      nr2,dr2=r2.number,r2.denom
      return Rational(nr1*nr2,dr1*dr2)

def MulInt(n1,n2):
     return n1*n2

def MulIntRational(n,r1):
      nr1,dr1=r1.number,r1.denom
      return Rational(n*nr1,dr1)

def type_tag(x):
 		return type_tag.tags[type(x)]

type_tag.tags={Rational:'rational',tuple:'rlist',int:'int'}

def add(z1,z2):
     types=(type_tag(z1),type_tag(z2))
     return add.implementations[types](z1,z2)

def mul(z1,z2):
     types=(type_tag(z1),type_tag(z2))
     return mul.implementations[types](z1,z2)

def apply(operator_name, x, y):
 		tags = (type_tag(x), type_tag(y))
 		key = (operator_name, tags)
 		return apply.implementations[key](x, y)

add.implementations={}

apply.implementations={('add',('rational','rlist')):AppendRlist,
                        ('add',('rlist','rlist')):MergeRlist,
                        ('add',('rational','rational')):AddRational,
                        ('add',('int','int')):AddInt,
                        ('add',('int','rational')):SumIntRational,
                        ('mul',('int','rlist')):MUltiplyRlist,
                        ('mul',('rational','rational')):MulRational,
                        ('mul',('int','int')):MulInt,
                        ('mul',('int','rational')):MulIntRational,
                       
                        ('+',('rational','rlist')):AppendRlist,
                        ('+',('rlist','rlist')):MergeRlist,
                        ('+',('rational','rational')):AddRational,
                        ('+',('int','int')):AddInt,
                        ('+',('int','rational')):SumIntRational,
                        ('*',('int','rlist')):MUltiplyRlist,
                        ('*',('rational','rational')):MulRational,
                        ('*',('int','int')):MulInt,
                        ('*',('int','rational')):MulIntRational}

#print("\n")
L1=make_rlist(1,None)
R1=Rational(2,4)
R2=Rational(3,2)
#print(AppendRlist(R1,L1))
L2=make_rlist(5,make_rlist(6,None))
#print(MergeRlist(L1,L2))
#print(AddRational(R1,R2)) 
#print(apply('*',4,L2))
