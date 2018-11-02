#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 2018-11-02 14:37
# @Author  : SunWang
# @File    : 循环.py


# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)


#计算1-10的整数之和
'''
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)
'''

#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
#print(list(range(5)))

#计算1-100的整数之和
'''
sum = 0
for num in list(range(101)):
    sum = sum + num
print(sum)
'''

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
'''
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print(sum)
'''

#请利用循环依次对list中的每个名字打印出Hello, xxx!：
'''
L = ['Bart', 'Lisa', 'Adam']
for name in L :
    print('Hello,',name,'!')
'''

#break
#在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
'''
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
'''
# 执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。
# 可见break的作用是提前结束循环。

#continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
# 上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

