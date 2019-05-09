'''
title：输入年份判断是不是闰年
author：瓜瓜
time：2019-5-9
'''

year = int(input("请输入年份："))
if (year%4 == 0 and year%100 != 0) or (year%4 == 0 and year%400 == 0):
    print("%s是闰年" % year)
else:
    print("%s不是闰年" % year)
