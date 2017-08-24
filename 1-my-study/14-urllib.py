#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


from urllib import request
from bs4 import BeautifulSoup

with request.urlopen('https://www.python.org/events/python-events/') as f:
    soup = BeautifulSoup(f, 'lxml', from_encoding='utf-8')
    fp = soup.section.text
    print((fp.split('More')[1]).split('You just missed...')[0])
