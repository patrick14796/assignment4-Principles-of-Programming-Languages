#Patrick Lugassy 319266177
#Ivan Borisenco  317366102

#def make_instance(cls):
#		"""Return a new object instance, which is a dispatch dictionary."""
#		attributes = {}
#		def get_value(name):
#		    if name in attributes:
#		        return attributes[name]
#		    else:
#		        value = cls['get'](name)
#		        return bind_method(value, instance)
#		def set_value(name, value):
#		    attributes[name] = value
#		instance = {'get': get_value, 'set': set_value}
#		return instance

#def bind_method(value, instance):
#    """Return a bound method if value is callable, or value otherwise."""
#    if callable(value):
#        def method(*args):
#            return value(instance, *args)
#        return method
#    else:
#            return value

#def make_class(attributes, base_class=None):
#    """Return a new class,which is a dispatch dictionary"""
#    def get_value(name):
#        if name in attributes:
#            return attributes[name]
#        elif base_class is not None:
#            return base_class['get'](name)
#    def set_value(name,value):
#        attributes[name]=value
#    def new(*args):
#        return init_instance(cls,*args)
#    cls={'get':get_value,'set':set_value,'new':new}
#    return cls

#def init_instance(cls,*args):
#    """return a new object with type CLS,initialized with args"""
#    instance=make_instance(cls)
#    init=cls['get']('__init__')
#    if init:
#        init(instance,*args)
#    return instance


#def make_MyDate_class():
#    def __init__(self, _day=0,_month=0,_year=2020):
#        if _day >= 1 and _day <= 30:
#            self['set']('day',_day)
#        if _month >= 1 and _month <= 12:
#            self['set']('month',_month)
#        if _year >= 1900 and _year <=2100: 
#            self['set']('year',_year)

#    def __repr__(self):
#        return{'day':self['get']('day'),'month':self['get']('month'),'year':self['get']('year')}
    
#    def __str__(self):
#        return str(self['get']('day'))+'.'+str(self['get']('month'))+'.'+str(self['get']('year'))


#    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__})



#def make_Person_class():
#    def __init__(self,_FirstName,_LastName,_DOB,_ID):
#        self['set']('FirstName',_FirstName)
#        self['set']('LastName',_LastName)
#        self['set']('DoB',_DOB)
#        if _ID>0:
#            self['set']('ID',_ID)

#    def __repr__(self):
#        return {'FirstName':self['get']('FirstName'),'LastName':self['get']('LastName'),'DoB':self['get']('DoB'),'ID':self['get']('ID')}

#    def __str__(self):
#        return ('Name:'+self['get']('FirstName')+' ' + self['get']('LastName') +'\n'
#                'DoB:' + self['get']('DoB')['get']('__str__')() + '\n' 
#                'ID:'+str(self['get']('ID')))
      
            
#    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__})



#def make_Student_class( personClass):

#    def __init__(self,_Department,_Average,_Seniority):
#        self['set']('Department',_Department)
#        self['set']('Average',_Average)
#        self['set']('Studying Seniority',_Seniority)

#    def __repr__(self):
#        return {'Department':self['get']('Department'),'Average':self['get']('Average'),'Studying Seniority':self['get']('Studying Seniority')}

#    def __str__(self):
#         return ((personClass['get']('__str__')())+'\n'
#                 'Learning:'+self['get']('Department')+'\n'
#                 'Avg:' +str(self['get']('Average'))+'\n'
#                 'Studying Seniority:'+str(self['get']('Studying Seniority')))

#    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__})


#def make_Faculty_class(personClass):

#    def __init__(self,_Teaching,_Salary,_Seniority):
#        self['set']('Teaching',_Teaching)
#        self['set']('Salary',_Salary)
#        self['set']('Teaching Seniority',_Seniority)
    
#    def __repr__(self):
#        return {'Teaching':self['get']('Teaching'),'Salary':self['get']('Salary'),'Teaching Seniority':self['get']('Teaching Seniority')}

#    def keys_values(self):
#        return ( 'Teaching:' + self['get']('Teaching')+ '\n'
#                'Salary:' + str(self['get']('Salary'))+'\n'
#                'Seniority:' + str(self['get']('Teaching Seniority')))

#    def __str__(self):
#        return ((personClass['get']('__str__')())+'\n'
#                'Teaching:' + self['get']('Teaching')+ '\n'
#                'Salary:' + str(self['get']('Salary'))+'\n'
#                'Seniority:' + str(self['get']('Teaching Seniority')))
   
#    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__})



#def make_TA_class(studentClass,facultyClass):
    
#    def __init__(self):
#        pass
    
#    def __repr__(self):
#        return 
      
#    def __str__(self):
#       return ((studentClass['get']('__str__')())+'\n'+
#                str(facultyClass['get']('keys_values')()))
    
#    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__})

#Date=make_MyDate_class()
#myDate=Date['new'](14,7,1996)
##print(myDate['get']('__repr__')())
#person=make_Person_class()
#p=person['new']('Patrick','Lugassy',myDate,312131145)
##print(p['get']('__str__')())

#ab=make_Student_class(p)
#ivan=ab['new']('Software Engineering' ,85.3 ,1)
##print(ivan['get']('__str__')())


#person2=make_Person_class()



#koko=make_TA_class(ivan,HavaFacult2)
#koko2=koko['new']()
#print(koko2['get']('__str__')())











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


#TODO
def MUltiplyRlist(n,l1):
      pass


    

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


#adders = add.implementations.items()
#apply.implementations.update({('+', tags):fn for (tags, fn) in adders})



#L1=make_rlist(1,make_rlist(2,make_rlist(3,None)))
L1=make_rlist(1,None)
R1=Rational(2,4)
R2=Rational(3,2)
#print(AppendRlist(R1,L1))
L2=make_rlist(5,make_rlist(6,None))
#print(MergeRlist(L1,L2))
#print(AddRational(R1,R2))
 
print(apply('+',4,R2))

