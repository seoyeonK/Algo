# https://www.acmicpc.net/problem/3460

T = int(input())
 
for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i - 1] == '1':
            print(i, end=' ')

