#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
print(md5.digest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
print(sha1.digest())
print('\r\n')

# name    | password
# --------+----------
# michael | 123456
# bob     | abc999
# alice   | alice2008
# 
# username | password
# ---------+---------------------------------
# michael  | e10adc3949ba59abbe56e057f20f883e
# bob      | 878ef96e86145580c38c87f0410ad153
# alice    | 99b1c2188db85afee403b1536010c2c9

def calc_md5(password):
	md5 = hashlib.md5();
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(username, password):
	if username not in db:
		print ('Username is not correct, please input the right one!')
		return db.get(username, False)
	passwd = calc_md5(password)
	if db[username] == passwd:
		return True
	else:
		return False

def login_with_salt(username, password):
	if username not in db:
		print ('Username is not correct, please input the right one!')
		return db.get(username, False)
	passwd = calc_md5(password + username + 'the-Salt')
	if db[username] == passwd:
		return True
	else:
		return False

def register(username, password):
    db[username] = calc_md5(password + username + 'the-Salt')

# exercise with defaultdict
from collections import defaultdict
ddb = defaultdict(lambda : 0)

def register(username, password):
	ddb[username] = calc_md5(password + username + 'the-Salt')

def login2(username, password):
	md5_user = calc_md5(password + username + 'the-Salt')
	if ddb[username] == 0:
		print('用户名%s不存在' % username)
	elif md5_user == ddb[username]:
		print('%s登陆成功' % username)
	else:
		print('密码错误，登陆失败')

if __name__ == '__main__':
# exercise 1
	#password = input('Please input password:')
	#print('The md5 hexdigest of your password is:')
	#print(calc_md5(password))
# exercise 2
	username = input('Please input your username:')
	password = input('Please input your password:')
	print('Your password is:',login(username, password))
# exercise 3
	username = input('Register a new username now\r\nPlease input your username:')
	password = input('Please input your password:')
	register(username, password)
	username = input('Login now\r\nPlease input your username:')
	password = input('Please input your password:')
	print('Your password is:',login_with_salt(username, password))
# exercise 4
	register('michael','123456')
	register('bob','abc999')
	register('alice','alice2008')
	login2('michael.','123456')
	login2('bob','abc999.')
	login2('alice','alice2008')
