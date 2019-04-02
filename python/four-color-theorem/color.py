#!/usr/bin/env python3
# encoding: utf-8

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
        self.colors = colors_limit

    def solve(self, i, ans):
        if i >= len(self.data):
            return ans

        used = list()
        for j in range(i):
            if self.data[j][i] == 1: # 检测到之前涂色的点
                if ans[i] != -1: # 与该国家相邻的国家已经被涂色
                    if not ans[i] in used:
                        used.append(ans[i]) # 将国家的颜色添加到已用颜色列表
                        print(used)
                else: # 该国家未被涂色
                    for color in self.colors:
                        if not color in used:
                            ans[i] = color # 选择一个周围国家未使用的颜色给该国家涂色
                            self.solve(i+1, ans+[])

                    if ans[i] == -1: # 没有可用的颜色，此种涂色方案不可行
                        return False
        return ans

if __name__ == '__main__':
    filename = 'color.dat'
    data = readData(filename)
    print_matrix(data)

    ans = [-1 for i in range(len(data))]
    s = Solution(data, 4)
    ans = s.solve(0, ans)
    print(ans)
