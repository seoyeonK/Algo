# 한개의 회의실, N개의 회의 
# 각 회의 I : 시작 시간, 끝나는 시간 회의 최대 개수?
# 회의 끝나자마자 다음 회의 가능, 시작시간과 끝시간 같을 수 있음
# https://suri78.tistory.com/26


#greedy

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

#끝나는 시간 오름차순 정렬 -> 시작하는 시간 오름차순

meets.sort(key = lambda x : (x[1], x[0]) )

count = 1
endtime = meets[0][1]

for i in range(1, n):
    if meets[i][0] >= endtime:
        count += 1
        endtime = meets[i][1]

print(count)