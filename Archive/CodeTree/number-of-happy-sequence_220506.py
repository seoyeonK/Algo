import sys
n, m = map(int, sys.stdin.readline().split())

grid = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

def compare_row(i,j, m):
    if i == n-1:
        return True
    if grid[i][j] == grid[i+1][j]:
        compare_row(i+1, j)
    else:
        return False

def compare_col(i,j):
    if j == n-1:
        return True
    if grid[i][j] == grid[i][j+1]:
        compare_col(i, j+1)
    else:
        return False

cnt = 0

for i in range(n):
    if compare_row(i,0):
        cnt +=1
    if compare_col(0,i):
        cnt +=1

print(cnt)
