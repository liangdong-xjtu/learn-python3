#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager
from collections import Iterable

@contextmanager
def log(name):
    print('[%s] start...' % name)
    yield
    print('[%s] end.' % name)

with log('DEBUG'):
    print('Hello, world!')
    print('Hello, Python!')

# 关于 with 上下文管理器的错误捕获，method 1
print('# 关于 with 上下文管理器的错误捕获，method 1')
@contextmanager
def closing(fname):
    f = None
    try:
        f = open(fname, 'r')
    except FileNotFoundError as e:
        print('except: FileNotFoundError', e)
        #若抛出异常，则程序无法继续执行，并非错误捕获的初衷
        #raise FileNotFoundError('No such file or directory: %s' % fname) 
    except IOError as e:
        print('except: IOError', e)
    except:
        print('except: Error', e)
    finally:
        if f:
           yield f
        try:
            if f:
                f.close()
        except IOError as e:
            print('except: IOError', e)
        except:
            print('except: Error', e)
try:
    with closing('test.txt') as f:
        try:
            if f:
                print(f.read())
        except IOError as e:
            print('except: IOError', e)
        except:
            print('except: Error', e)
except RuntimeError as e:
    print('except: RuntimeError', e)
    print('except: RuntimeError generator didn\'t yield')
    #若抛出异常，则程序无法继续执行，并非错误捕获的初衷
    #raise RuntimeError("generator didn't yield") from None 
except:
    print('except: Error', e)

# 关于 with 上下文管理器的错误捕获，method 2
print('# 关于 with 上下文管理器的错误捕获，method 2')
@contextmanager
def closing(fname):
    f = None
    try:
        f = open(fname, 'r')
    except FileNotFoundError as e:
        print('except: FileNotFoundError', e)
        #若抛出异常，则程序无法继续执行，并非错误捕获的初衷
        #raise FileNotFoundError('No such file or directory: %s' % fname) 
    except IOError as e:
        print('except: IOError', e)
    except:
        print('except: Error', e)
    finally:
        yield f  # always yield f, 则后面无需处理 RuntimeError 'generator didn\'t yield'
        try:
            if f:
                f.close()
        except IOError as e:
            print('except: IOError', e)
        except:
            print('except: Error', e)
with closing('test.txt') as f:
    try:
        if f:
            print(f.read())
    except IOError as e:
        print('except: IOError', e)
    except:
        print('except: Error', e)

# 关于 with 上下文管理器的错误捕获，method 3
print('# 关于 with 上下文管理器的错误捕获，method 3')
@contextmanager
def closing(fname):
    f = None
    try:
        f = open(fname, 'r')
    except FileNotFoundError as e:
        print('except: FileNotFoundError', e)
        #若抛出异常，则程序无法继续执行，并非错误捕获的初衷
        #raise FileNotFoundError('No such file or directory: %s' % fname) 
    except IOError as e:
        print('except: IOError', e)
    except:
        print('except: Error', e)
    finally:
        yield f  # always yield f, 则后面无需处理 RuntimeError 'generator didn\'t yield'
        try:
            if f:
                f.close()
        except IOError as e:
            print('except: IOError', e)
        except:
            print('except: Error', e)
with closing('test.txt') as f:
    try:
        print(f.read())
    except AttributeError as e:
        print('except: AttributeError', e)
    except IOError as e:
        print('except: IOError', e)
    except:
        print('except: Error', e)


# 生成器
print('######### 生成器 generator:')
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fib(10):
    print (n)

g = (x * x for x in range(10))
print(g)
for i in range(10):
    print(next(g))

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break   #watch out, 每个except都要有个break，结束循环
    except: # 最后再加一个default处理，增强鲁棒性
        print('except: Error', e)
        break   #watch out, 每个except都要有个break，结束循环

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))
