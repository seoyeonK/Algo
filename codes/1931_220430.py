# 한개의 회의실, N개의 회의 
# 각 회의 I : 시작 시간, 끝나는 시간 회의 최대 개수?
# 회의 끝나자마자 다음 회의 가능, 시작시간과 끝시간 같을 수 있음

"""input
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""
# output : 4

import sys

n = int(sys.stdin.readline())

meets = []

for i in range(n):
    meets.append(list(map(int, sys.stdin.readline().split())))

meets.sort(key = lambda x :  )
    
