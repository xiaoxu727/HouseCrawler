from JiNanHouse.utils import format
from datetime import datetime
from JiNanHouse.items import ftx_residential_baseinfo_item
import codecs
import os
# url = 'https://jn.lianjia.com/xiaoqu/pg%dcro21/'
# # for i in range(1, 101):
# #     print("'"+ url % i +"',")
# #
# start_urls = ['https://jn.lianjia.com/xiaoqu/pg%dcro21/' % i for i in range(1, 101)]
# print(start_urls)
#
# print('a' if 7 > 2 else 'b')
#
# arr = ['a', 'b']
# print(len(arr))
#
# url = 'http://lingxiuchengjnln.fang.com/esf/'
# url = 'http://yanshanxiaoqu0531.fang.com/'
#
# print(datetime.now().strftime('%Y-%m-%d'))
#  __new__() 与__init__()区别
# 继承自object的新式类才有__new__
#
# __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
#
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
#
# __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
#
# 若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的，即使是父类的实例也不行

class B(object):
    def fn(self):
        print('B fn')
    def __init__(self):
        print("B INIT")

    def __new__(cls):
        print('B new')
        return super(B, cls).__new__(cls)



class A(B):
    def fn(self):
        print('A fn')

    def __new__(cls, a):
            print("NEW", a)
            if a > 10:
                return super(A, cls).__new__(cls)

                # return object.__new__(cls)
            return B()

    def __init__(self, a):
        print("INIT", a)
#
# # a1 = A(5)
# # a1.fn()
# a2 = A(20)
# a2.fn()
# print(type(a2))

# 集成类调用顺序
# mro排列继承顺序
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        print(self.__class__)
        super(A, self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print(self.__class__)
        print("leave C")

    # def __next__(self):



# b = B()

# pritn(B())

# c = C()
# print(c.__class__)
# c.__class__ = B
# print(c.__class__)
# print(c.__init__())
#

#__call__
class Call():
    def __init__(self):
        print('INT')

    def __call__(self, *args, **kwargs):
         self.__init__()

# Call()



# 全局变量和局部变量

num = 1


def test():
    global num
    print(num)
    num = 3
    print(num)
#
# test()
# print(num)


# __getatrr__  __setatrr__
class tes2():

    def __getattr__(self, item):
        return self.default

    def __setattr__(self, key, value):
        self.default(key,value)

    def default(self, *args):
        print('exc')
        print(args)

t = tes2()
t.tt('tt')
t.tt = 'tt'

# 闭包
def mulby(num):
    def gn(val):
        return num * val

    return gn


zw = mulby(7)
# print(zw(9))


a = ['de ', 'das ']
b = ''.join([ format(i) for i in a])
# print(b)

# t = ['a'  for i in a if 'a' in i else '']
# set1 = {x for x in 'hello world' if x not in 'low level'}
set1 = [True for x in a if 'c' in x]
# print('小区地址' in '小区地址：')
# print(set1)


field_map = {'小区地址': 'address', '小所属区域': 'district'}
item = ftx_residential_baseinfo_item()
keys = [x for x in field_map if '小' in x]
# keys =['']
# for key in keys:
#     item[field_map[key]] = 'value'
# print(item)
# print(keys)
# item[field_map[keys]] = 'value'
str ='dd'
# print(str.endswith('d'))

file = codecs.open('test.txt', 'w')
print(file.name)
file.close()
if os.path.exists(file.name):
    os.remove(file.name)