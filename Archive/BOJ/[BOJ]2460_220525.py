# !~10 각 역에서 타고 내리는 사람 누적 count, 가장 많을 때의 사람 수 

import sys

max_pp = 0
total = 0

for _ in range(10):
    go, come = map(int, sys.stdin.readline().split())
    total = total + come - go
    max_pp = max(max_pp, total)

print(max_pp)