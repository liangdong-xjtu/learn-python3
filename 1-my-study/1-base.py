#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.python.org/dev/peps/pep-0263/
# use: # coding=<encoding name>
# use: # -*- coding: <encoding name> -*-
# use: # vim: set fileencoding=<encoding name> :
###########################################

#from selenium import webdriver
#import time
#
#driver = webdriver.Chrome()
#driver.get("http://www.baidu.com")
#time.sleep(2)

print unicode(100)
print str(100)

# list [1,2,3]
# tuple (1,)
# dict {A:B}
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d.get('Thomas')
print d.get('Thomas', -1)
print d
d.pop('Bob')
print d

s = set([1,2,3])
print s
s.add((1, 2, 3))
print s


# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
a = 'abc'
b = a.replace('a', 'A')
print b, a 

# http://blog.csdn.net/devil_2009/article/details/38796533
str1 = '\u4f60\u597d'
print str1.decode('unicode_escape')
###########################################

# An UTF-8 char is 3byte with \xXX\xXX\xXX
# \xe4 is 0xe4 int(0xe4)=228
# 如果你使用Notepad++进行编辑，除了要加上# -*- coding: utf-8 -*-外，中文字符串必须是Unicode字符串
# 由于历史遗留问题，Python 2.x版本虽然支持Unicode，但在语法上需要'xxx'和u'xxx'两种字符串表示方式。
# 在Python 3.x版本中，把'xxx'和u'xxx'统一成Unicode编码，即写不写前缀u都是一样的，而以字节形式表示的字符串则必须加上b前缀：b'xxx'。
print u'中文'.encode('utf-8')	# unicode -> utf-8
u'中文'.encode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'
len('\xe4\xb8\xad\xe6\x96\x87')
u'A'
u'中'
print u'中文'
print chr(65)
print ord('A')
print u'Hi, %s' % u'Michael'
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)

print int(0b00110000)

print r'''test1
test2
test3
\\t'''

# test raw_input
#a=raw_input('please enter a number:')
#
#if int(a)>=100:
#    print a
#else:
#    print -1*int(a)
##    print '-'+a
