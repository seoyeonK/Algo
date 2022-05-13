# https://www.acmicpc.net/problem/3460

import sys
T = int(sys.stdin.readline())


for i in range(T):
    num =  int(sys.stdin.readline())
    for i in range(len(num)):
        if num[-i - 1] == '1':
            print(i, end=' ')
