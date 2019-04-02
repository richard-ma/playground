#!/usr/bin/env python3
# encoding: utf-8

import sys

def readData(filename):
    filedata = list()
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            d = list(map(int, list(line.split(' '))))
            filedata.append(d)

    filedata.append(list())
    l = len(filedata)

    data = [[0 for i in range(l)] for j in range(l)]

    for i, node in enumerate(filedata):
        for n in node:
            data[i][n-1] = 1

    return data

def print_matrix(matrix):
    r = len(matrix)
    c = len(matrix[0])

    print("%8s" % (' '), end='')
    for j in range(c):
        print("%4d" % (j), end='')
    print()

    for i in range(r):
        print("%4d%4s" % (i, '|'), end='')
        for j in range(c):
            print("%4d" % (matrix[i][j]), end='')
        print()

class Solution():
    def __init__(self, data, colors_limit):
        self.data = data
        self.colors = list(range(colors_limit))

    def solve(self, i, ans):
        if i >= len(self.data):
            return ans

        used = set()
        for j in range(i):
            if self.data[j][i] == 1: # 检测到之前涂色的点
                if ans[j] != -1: # 与该国家相邻的国家已经被涂色
                    if not ans[j] in used:
                        used.add(ans[j]) # 将相邻国家的颜色添加到已用颜色列表
        print(used)

        for color in self.colors:
            if not color in used:
                ans[i] = color # 选择一个周围国家未使用的颜色给当前未涂色的国家涂色
                return self.solve(i+1, ans+[]) # 处理完当前国家，处理下一个国家

        if ans[i] == -1: # 颜色用光了，此种涂色方案不可行
            return False

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else 'color.dat'
    data = readData(filename)
    print_matrix(data)

    ans = [-1 for i in range(len(data))]
    s = Solution(data, 4)
    ans = s.solve(0, ans)
    print(ans)
