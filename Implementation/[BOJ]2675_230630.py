import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().split()
    R_ = int(R)
    result = ''
    for s in S:
        result += s * R_
    
    print(result)