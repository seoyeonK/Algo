from collections import deque

N = int(input())
M = int(input())

co = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    co[x].append(y)
    co[y].append(x)

visited = [0] * (N+1)

def bfs():
    visited[1] = 1
    queue = deque((1))

    while queue:
        x = queue.popleft()
        for y in co[x]:
            if not visited[y]:
                queue.append(y)
                visited[y] = 1

