# import sys

# n = int(sys.stdin.readline())

# nums = list(map(int, sys.stdin.readline().split()))
# ops = list(map(int, sys.stdin.readline().split())) # + , -, *, /

# MAX = -1000000000
# MIN = 1000000000



#SOLUTION - 백트래킹 or 순열
#https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python
#1. 백트래킹(DFS)

import sys
N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline()))
op = list(map(int, sys.stdin.readline()))

maxi = -1e9 #10billion
mini = 1e9 #-10billion

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)


#2. 순열 (Python3 시간초과 / PyPy3는 통과)
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))  # +, -, *, /
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

maximum = -1e9
minimum = 1e9


def solve():
    global maximum, minimum
    for case in permutations(op, N - 1):
        total = num[0]
        for r in range(1, N):
            if case[r - 1] == '+':
                total += num[r]
            elif case[r - 1] == '-':
                total -= num[r]
            elif case[r - 1] == '*':
                total *= num[r]
            elif case[r - 1] == '/':
                total = int(total / num[r])

        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total


solve()
print(maximum)
print(minimum)

