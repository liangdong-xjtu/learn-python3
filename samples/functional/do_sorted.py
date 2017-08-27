#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda x: x[0].lower()))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
# 甚至我们可以先对元组的第2个元素进行排序，然后对第一个元素进行排序，形成多级排序
print(sorted(students, key=itemgetter(1,0), reverse=True))

grade={'Lina':54,'Green':75,'Bob':79}
print(sorted(grade,key=lambda x:x[0]))
print(sorted(grade,key=lambda x:(str(x[0]).lower())))
print(sorted(grade,key=lambda x:x[1])) # 答案无法解释 ???
