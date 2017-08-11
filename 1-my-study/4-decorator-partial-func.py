#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
log(now)()
log(log(now))()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

#today = logger('DEBUG')(today)
#f = logger('DEBUG')(today)
f = logger('DEBUG')(logger('DEBUG')(today))

today()
#print(today.__name__)
f()
#print(f.__name__)

def int2(x, base=2):
   return int(x, base)

int2 = functools.partial(int, base=2)
print int2('100')
print int2('100', base=10)

max2 = functools.partial(max, 10) 
print max2(5,6,7)
#实际上会把10作为*args的一部分自动加到左边，也就是：
# args = (10, 5, 6, 7)
# max(*args)
