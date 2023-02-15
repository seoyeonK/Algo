# a, b = map(int, input().split())
# c = [i for i in range(1, a+1) if a%i==0]
# print(0 if len(c)<b else c[b-1])


import sys

n, k = map(int, sys.stdin.readline().split())

cnt = 0

for i in range(1, n+1):
    if( n % i == 0 ):
        cnt += 1
        if(cnt == k):
            print(i)
if(cnt < k):
    print("0")