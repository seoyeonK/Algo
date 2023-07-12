import math
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    students = list(map(int, input().split()))
    B, C = map(int, input().split())

    supervisor = N

    studs = [ x-B for x in students ]

    for s in studs:
        if 0 < s :
            supervisor += math.ceil(s / C)

    print(supervisor)

solution()