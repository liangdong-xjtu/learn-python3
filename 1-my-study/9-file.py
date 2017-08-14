#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

try:
    f = open('./xreg_splash.bmp', 'rb')
#    print(f.read())
finally:
    if f:
        f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open('./xreg_splash.bmp', 'rb') as f:
#	print(f.read())
	pass

#with open('./xreg_splash.bmp', 'rb') as f:
#	for line in f.readlines():
#		print(line.strip()) # 把末尾的'\n'删掉

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
print(os.path.abspath('/home/dong'))

print(os.path.join('/home', 'dong'))
os.mkdir('./testdir')
os.rmdir('./testdir')
print(os.path.split('/Users/michael/testdir/file.txt'))

import shutil
shutil.copyfile('./xreg_splash.bmp', './xreg_splash_copy.bmp')
os.remove('./xreg_splash_copy.bmp')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

with open('./utf-8.txt', 'w', encoding='utf-8') as f:
	f.write('测试')
with open('./utf-8.txt', 'r', encoding='gbk', errors='ignore') as f:
	print(f.read())
with open('./utf-8.txt', 'r', encoding='utf-8', errors='ignore') as f:
	print(f.read())
os.remove('./utf-8.txt')

