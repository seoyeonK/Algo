import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    words = list(set([ input().rstrip() for _ in range(N) ]))
    words.sort(key=lambda x: (len(x), x))
    print(*words, sep='\n')
    return

solution()