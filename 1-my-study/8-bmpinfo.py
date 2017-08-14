#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct, os

def checkbmp(path):
	if os.path.splitext(path)[1] == '.bmp':
		with open(path,'rb') as f:
			i = 0
			s = b''
			while True:
				byte = f.read(1)
				if byte:
					i += 1
#					print(i)
				else:
					print('The file is not a bitmap.')
					break
				s = s+(byte)
				if i == 30:
					fileInfo = struct.unpack('<ccIIIIIIHH', s)
					print(s)
					print(fileInfo)
					if(fileInfo[0] == b'B' and fileInfo[1] == b'M'):
						print('The size of BitMap is %s * %s, #color is %s' % (fileInfo[6], fileInfo[7], fileInfo[9]))
						break
					else:
						print('The file is not a bitmap.')
						break

if (__name__ == '__main__'):
#	path = input('input BMP file:')
	path = './xreg_splash.bmp'
	checkbmp(path)
	path = './xreg_splash_1.bmp'
	checkbmp(path)
	path = './xreg_splash_2.bmp'
	checkbmp(path)

