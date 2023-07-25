import sys
input = sys.stdin.readline

def solution():
    T = int(input())

    for _ in range(T):
        A, B = map(int, input().split())
        print(lcm(A,B))

def gcd(A,B):
    while B > 0:
        A, B = B, A % B
    
    return A

def lcm(A,B):
    return A * B // gcd(A, B)

solution()