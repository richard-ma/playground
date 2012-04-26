#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用floyd法计算PI的值
#
# 以(0, 0)点为圆心，半径5个单位长度做圆
# 做这个圆的外接矩形（实际是个外接正方形）
# 只观察第一象限
# 圆的面积 = (PI * r * r) / 4
# 外接正方形的面积 = (2 * r) * (2 * r) / 4
#
# 随机产生第一象限内在(0, 0)到(5, 5)为对角顶点的矩形范围内的坐标
# 判断坐标是否落在圆内或圆上，计数
#
# 落入圆内与落入1/4矩形面积之比为1/4圆和1/4外接正方形面积之比，即PI / 4 : 1
# PI 为这个比值的4倍

import math
import random

times = 1000000 # 不断加大这个值，PI的精度会更高，但运算时间更长
# 这个次数，精度基本保持在百分位，不过有时会出现精度较低的特殊情况

in_cnt = 0
for cnt in xrange(times):
# 产生随机坐标
    x = random.uniform(0, 5)
    y = random.uniform(0, 5)

# 判断是否在圆内或圆上
    if x * x + y * y - 25 <= 0:
        in_cnt += 1

print 4.0 * in_cnt / times
