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

    def __repr__(self):
        return{'day':self['get']('day'),'month':self['get']('month'),'year':self['get']('year')}
    
    def __str__(self):
        return str(self['get']('day'))+'.'+str(self['get']('month'))+'.'+str(self['get']('year'))


    return make_class({'__init__': __init__, '__repr__':__repr__ , '__str__':__str__})







Date=make_MyDate_class()
myDate=Date['new'](1,1,1958)
print(myDate['get']('__repr__')())