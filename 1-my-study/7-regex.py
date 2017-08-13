#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 用\d可以匹配一个数字，\w可以匹配一个字母、数字、下划线
# .可以匹配任意字符
# 要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格
# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束

m = re.match(r'^(\d+)(0*)$', '102300').groups()
print(m)
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
m = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(m)


m = re.match(r'(ABC)-(001)','ABC-001')
print(m)
print(m.group(1), m.group(2))

## TODO: need to be checked
m = re.match('\w{3}\\\-\d{3}','ABC\\-001')
print(m)
m = re.match('\w{3}\\\-\d{3}',r'ABC\-001')
print(m)
m = re.match(r'\w{3}\\\-\d{3}',r'ABC\-001')
print(m)
m = re.match(r'\w{3}\\-\d{3}',r'ABC\-001')
print(m)
m = re.match(r'\w{3}\\-\d{3}','ABC\-001')
print(m)
m = re.match('\w{3}\\\-\d{3}','ABC\-001')
print(m)


t = '2-30'
print('Test:', t)
m = re.match('^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$', t)
print(m.groups())

m = re.match('[a-zA-Z\_][0-9a-zA-Z\_]*', 'a')
print(m)

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

re_email_1 = re.compile(r'(\w+|\w+.\w+)@(\w+).com')
#re_email_1 = re.compile(r'^[a-z0-9][a-z0-9\_\.]+@[a-z0-9]+.[a-z]{2,6}')
re_email_1 = re.compile(r'(\w.+)@(\w.+)')
t1 = 'someone@gmail.com'
t2 = 'bill.gates@microsoft.com'
t3 = 'bill19.gates@intel.com.cn'
t4 = 'bill_19_xjtu.mail@stu.xjtu.edu.cn'
t5 = 'bill_19.gates.good_xjtu@intel.org.vog'
print(re_email_1.match(t1).groups())
print(re_email_1.match(t2).groups())
print(re_email_1.match(t3).groups())
print(re_email_1.match(t4).groups())
print(re_email_1.match(t5).groups())

# 版本二可以验证并提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org
re_email_2 = re.compile(r'^<(\w.+)>\s+?(\w.+)@(\w.+)')
t6 = '<Tom Paris> tom@voyager.org'
print(re_email_2.match(t6))
print(re_email_2.match(t6).groups())





