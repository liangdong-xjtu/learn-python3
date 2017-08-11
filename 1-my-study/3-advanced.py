#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
for k, v in d.iteritems():
    print k, v

for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1,1), (2,4), (3,9)]:
    print x, y

L = []
for x in range(1, 11):
   L.append(x * x)
print L

# 列表生成式
L = [x * x for x in range(1, 11)]
print L
L = [x * x for x in range(1, 11) if x % 2 == 0]
print L

L = [m + n for m in 'ABC' for n in 'XYZ']
print L

import os
L = [d for d in os.listdir('.')]
print L

d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k + '=' + v for k, v in d.iteritems()]
print L

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]

# 生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
	yield b
	a, b = b, a + b
	n = n + 1
for n in fib(10):
        print n

# 函数式编程 高阶函数
def add(x, y, f):
    return f(x) + f(y)
print add (-5, 6, abs)

# map/reduce
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def add(x, y):
    return x+y
reduce(add, [1, 3, 5, 7, 9])

def f(x, y):
    return x * 10 + y
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
print reduce (f, map(char2num, '13579'))
# str2int 函数定义
def str2int(s):
    def f(x, y):
	return x * 10 + y
    def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
    return reduce (f, map(char2num, s))
print str2int('13579')

# 最简单的两行 str2int
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(lambda c:ord(c)-48,s))

# 练习：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
L = ['adam', 'LISA', 'barT']
def norm(s):
    str = ''
    str = str+s[0].upper()
    for c in s[1:]:
	str = str+c.lower()
    return str
print map(norm, L)

def normalize(s):
    return(s[0].upper() + s[1:].lower())
print map(normalize, ['adam', 'LISA', 'barT'])

def norm(x):
    if not isinstance(x, str):
        raise TypeError('input is not string')
    if len(x) < 2:
        raise TypeError('The name is too short')
    return x[0].upper() + x[1:].lower()
if __name__ == '__main__':
    names = ['adam', 'LISA', 'barT']
    normed_names = map(norm, names)
    print normed_names

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
L = [1,3,5,7,9]
def prod(L):
    def mul(x, y):
	return x * y
    return reduce(mul, L)
print prod(L)

# filter
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])


# 请尝试用filter()删除1~100的素数。
#def is_prime(s):
#    if not isinstance(s, int):
#	raise TypeError('bad operand type') 
#    L = range(s).pop().pop(0)
#    def aliquot(x, y):
#	return x % y == 0
#    def f(x, y):
#	return x or y
#    return not reduce(f, map(aliquot(s), L))

#def is_not_prime(s):
#    if not isinstance(s, int):
#	raise TypeError('bad operand type')
#    if s <= 1:
#	raise TypeError('input should be >= 2')
#    if s == 2:
#	return 1;
#    #L = range(s).pop().pop(0)
#    L = range(s)[1:-1]
#    def aliquot_1(x, y):
#	return x % y == 0
#    def f(x, y):
#	return x and y
#    def aliquot(y):
#	return aliquot_1(s, y)
#    return not reduce(f, map(aliquot, L))

# 闭包函数 https://www.zhihu.com/question/52188800/answer/130921785

print range(2, 4)
L1 = range(0, 100)
def is_prime(s):
    if not isinstance(s, int):
	raise TypeError('bad operand type')
    if s <= 1:
	raise TypeError('input should be >= 2')
    if s == 2:
	return 1;
#    L = range(1, s+1)[1:-1]
#    L = L1[2:s]
#    print 'L =', L
    def aliquot(y):
	return s % y == 0
    def f(x, y):
	return (x or y)
    return not reduce(f, map(aliquot, L1[2:s]))
def is_not_prime(s):
    return not is_prime(s)
print filter(is_not_prime, range(2, 101))
#print filter(not is_prime, range(100)) # This can't be used


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


