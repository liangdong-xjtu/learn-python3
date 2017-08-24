#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())


class Student(object):
    name='Student'
    def __init__(self,name):
        self.name=name
s=Student('Bob')
print(s.name)#打印实例s的属性name
print(Student.name)#打印类Student的属性name
s.name='Mark'
print(s.name)
print(Student.name)
del s.name
print(s.name)
print(Student.name)


import json
class Student(object):
    name = "bob"
    age = 15
    sex = 1
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
s = Student("bob", 15 , 1)
print(json.dumps(s, default=lambda obj: obj.__dict__))


