#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 2018-11-14 13:42
# @Author  : SunWang
# @File    : 函数的参数.py

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
print(calc())

#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))

#这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Michael', 30))
print(person('Bob', 35, city='Beijing'))
print(person('Adam',45, gender='M', job='Engineer'))

extra = {'city': 'Beijing', 'job':'Engineer'}
print(person('Jack', 24, city=extra['city'] ,job=extra['job']))

#上面复杂的调用可以用简化的写法：
extra = {'city': 'Beijing', 'job':'Engineer'}
print(person('Jack', 24, **extra))

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
print(person('Jack', 24, city='Beijing', job='Engineer'))

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

print(person('Jack', 24, city='Beijing', job='Engineer'))

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

#由于命名关键字参数city具有默认值，调用时，可不传入city参数：
print(person('Jack', 24, job='Engineer'))

#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少*,则city和job被视为位置参数。
    pass

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a = ', a , 'b= ' , b, 'c= ', c, 'args=', args, 'kw= ', kw)

def f2(a, b, c=0, * , d, **kw):
    print('a= ', a, 'b=', b, 'c=',c,'d=',d,'kw=',kw)

print(f1(1, 2))
#结果：a =  1 b=  2 c=  0 args= () kw=  {}
print(f1(1,2, c=3))
#结果：a =  1 b=  2 c=  3 args= () kw=  {}
print(f1(1,2,3,'a','b'))
#结果：a =  1 b=  2 c=  3 args= ('a', 'b') kw=  {}
print(f1(1,2,3,'a','b',x=99))
#结果：a =  1 b=  2 c=  3 args= ('a', 'b') kw=  {'x': 99}
print(f2(1,2,d=99, ext=None))
#结果：a=  1 b= 2 c= 0 d= 99 kw= {'ext': None}
args = {1,2,3,4}
kw = {'d':99,'x':'#'}
print(f1(*args, **kw))
#a =  1 b=  2 c=  3 args= (4,) kw=  {'d': 99, 'x': '#'}
args = (1,2,3)
kw = {'d':88 , 'x':'#'}
print(f2(*args, **kw))
#结果：a=  1 b= 2 c= 3 d= 88 kw= {'x': '#'}

#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
#虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

#练习：
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*kw):
    numbers=list(kw)
    sum = 1
    for num in numbers:
        sum *= num
    return sum

print(product(1,2,3,4,5,6,7,8,9))



