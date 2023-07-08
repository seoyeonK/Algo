from itertools import combinations
import sys

def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    cards = list(map(int, input().split()))

    three = list(combinations(cards,3))

    approx = 0

    for t in three:
        s = sum(t)
        if M >= s and approx < s:
            approx = s 

    print(approx)

solution()