# https://www.acmicpc.net/problem/3460

T = int(input())
 
for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i - 1] == '1':
            print(i, end=' ')

'''
T = int(input())
for _ in range(T):
    n = bin(int(input()))[2:]
    for idx, val in enumerate(n[::-1]):
        if val == '1':
            print(idx, end=' ')
'''
