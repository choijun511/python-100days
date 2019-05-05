'''
title：输入半径计算圆的周长和面积
author：瓜瓜
time：2019-5-5
'''

import math

raduis = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * raduis
area = math.pi * raduis * raduis
print ('周长：%.2f' % perimeter)
print ('面积：%.2f' % area)
