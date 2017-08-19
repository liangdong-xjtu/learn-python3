#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

print('Test 1.1')
natuals = itertools.count(1)
for n in natuals:
	print(n)
	if n >= 100:
		break

print('Test 1.2')
natuals = itertools.count(start=0, step=5)
for n in natuals:
	print(n)
	if n >= 100:
		break

print('Test 2.1')
cs = itertools.cycle('ABC')
t = 10
for c in cs:
	print(c)
	t = t - 1
	if t == 0:
		break

print('Test 2.2')
ns = itertools.repeat('A', 3)
for n in ns:
	print(n)

print('Test 3')
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

print('Test 4')
for c in itertools.chain('ABC', 'XYZ'):
	print(c)

print('Test 5')
for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print(key, list(group))


