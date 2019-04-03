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
        print("%4d" % (j+1), end='')
    print()
    print("-" * (c * 4 + 8))

    for i in range(r):
        print("%4d%4s" % (i+1, '|'), end='')
        for j in range(c):
            print(("%4d" % (matrix[i][j]) if matrix[i][j] else ("%4s" % (' '))), end='')
        print()
    print()

class Solution():
    def __init__(self, data, colors_limit):
        self.data = data
        self.l = len(self.data)
        self.colors = list(range(colors_limit))
        self.ans = list()

        self.counter = 0

    def solve(self, i, ans):
        if i >= self.l:
            self.ans.append(ans)
            self.print_running_status(True)
            return True

        used = set()
        for j in range(i):
            if self.data[j][i] == 1: # 检测到之前涂色的点
                if ans[j] != -1: # 与该国家相邻的国家已经被涂色
                    used.add(ans[j]) # 将相邻国家的颜色添加到已用颜色列表
        #print(used)

        for color in self.colors:
            if not color in used:
                ans[i] = color # 选择一个周围国家未使用的颜色给当前未涂色的国家涂色
                #print("%d:%s" % (i, ans))
                self.solve(i+1, ans+[]) # 处理完当前国家，处理下一个国家

        if ans[i] == -1: # 颜色用光了，此种涂色方案不可行
            self.print_running_status(False)
            return False

    def print_running_status(self, status):
        self.counter += 1
        if status:
            print("%d: ++记录一组解++" % (self.counter))
        else:
            print("%d: --排除一组解--" % (self.counter))

    def print_ans(self, ans_limit):
        print('\n')
        print("输入数据邻接矩阵")
        print_matrix(self.data)
        print("共进行%d次搜索，获得解%d个" % (self.counter, len(self.ans)))
        if ans_limit <= 0:
            ans_limit = len(self.ans)
            print("全部解")
        else:
            ans_limit = min(ans_limit, len(self.ans))
            print("前%d个解" % (ans_limit))

        for i in range(ans_limit):
            print(self.ans[i])

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else 'color.dat' # 设置输入文件
    ans_limit = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else 5 # 设置输出结果数量限制，0为全部输出
    colors_limit = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[2] else 4 # 设置颜色数量限制，默认为四色定理
    data = readData(filename)

    ans = [-1 for i in range(len(data))]
    s = Solution(data, colors_limit)
    s.solve(0, ans)
    s.print_ans(ans_limit)
