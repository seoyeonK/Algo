# https://www.codetree.ai/missions/2/problems/best-place-of-33/discussions/684

import sys

n = int(sys.stdin.readline())

grid = []


for i in range(n) : 
    grid.append(list(map(int, sys.stdin.readline().split())))

def cnt_coin(row, col):
    cnt = 0
    for i in range(row, row+3): 
        for j in range(col, col+3):
            cnt += grid[i][j]
    return cnt

max_cnt = -1

for i in range(n):
    for j in range(n):
        if i+2 >= n or j+2 >=n :
            continue
        max_cnt = max( cnt_coin(i, j), max_cnt)

print(max_cnt)