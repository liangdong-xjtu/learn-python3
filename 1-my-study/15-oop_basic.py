#!/usr/bin/env python3
# -*- coding: utf-8 -*-

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

############### 类和实例 ###############

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

############### 访问限制 ###############

# 动态语言特性：和静态语言不同，Python允许对实例变量绑定任何数据
bart.age = 8
print(bart.age)
#print(lisa.age)
print(bart._Student__name)


############### 继承和多态 ###############

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eating...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

a = Animal()
d = Dog()
c = Cat()

# 多态：因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(a)
run_twice(d)

# 动态语音特性：
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#  Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
class Timer(object):
    def run(self):
        print("Timer is running...")
t = Timer()
run_twice(t)
run_twice(Timer())

############### 获取对象信息 ###############

# 使用type()
# 基本类型都可以用type()判断
# 如果一个变量指向函数或者类，也可以用type()判断
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types
def fn():
    pass
print('type(fn) is types.FunctionType?', type(fn) == types.FunctionType)
print('type(fn) is %s', type(fn))
print('type(abs) is types.BuiltinFunctionType?', type(abs) == types.BuiltinFunctionType)
print('type(abs) is %s', type(abs))
print('type(lambda x: x) is types.LambdaType?', type(lambda x: x)==types.LambdaType)
print('type(lambda x: x) is %s', type(lambda x: x))
print('type((x for x in range(10))) is types.GeneratorType?', type((x for x in range(10)))==types.GeneratorType)
print('type((x for x in range(10))) is %s', type((x for x in range(10))))

# 使用isinstance()

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 判断一个变量是否是某个类型可以用isinstance()判断
print('a is Animal?', isinstance(a, Animal))
print('d is Animal?', isinstance(d, Animal))
print('a is Dog?', isinstance(a, Dog))

# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1, 2, 3], (list, tuple)))

# 使用dir()

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('ABC'))

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
         return 100
dog = MyDog()
print(len(dog))
print(dog.__len__())

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
setattr(obj, 'y', 19)
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 404))
fn = getattr(obj, 'power')
print(fn)
print(fn())

############### 实例属性和类属性 ###############
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到

class Stu(object):
    name = 'Stu' # 定义的类属性也可以通过del删除
    def __init__(self, name):
        self.name = name
s = Stu('Dong')
print(s.name)
print(Stu.name)
s.name = 'Bob' # 给实例属性赋新值
print(s.name) # 但是类属性并未消失
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(Stu.name)
Stu.name = 'Alice' # 给类属性赋新值
print(Stu.name)
del Stu.name
#print(Stu.name)

# 从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
# 就像java里面的静态成员变量，是属于这个类而不是某个个体的，但是python是允许你以这个名字为一个实例赋予新值而不会冲突，但是类的值是不会变的，直接为类的变量赋值他就会改变
# 类属性和实例属性是两个属性，只不过以实例变量取值存在优先级。


# 本节讨论区

# 序列化
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

