import sys
from collections import deque
    
def solution():

    input = sys.stdin.readline

    N, M = map(int, input().split())
    ladders = dict()
    snakes = dict()

    for _ in range(N):
        x, y = map(int, input().split())
        ladders[x] = y
    
    for _ in range(M):
        u, v = map(int, input().split())
        snakes[u] = v

    visited = [False] * 101

    rolls = 0

    #BFS
    cur = 1
    queue = deque()
    queue.append((cur, rolls))
    visited[1] = True
    
    while queue:
        cur, rolls = queue.popleft()
        if cur == 100:
            print(rolls)
            break

        for dice in range(1,7):
            next = cur + dice
            
            if next <= 100:
                if next in ladders.keys():
                    next = ladders[next]
                elif next in snakes.keys():
                    next = snakes[next]
                if not visited[next] :
                    queue.append((next, rolls+1))
                    visited[next] = True

solution()