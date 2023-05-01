from collections import deque


n = int(input())

graph = [ [] for _ in range(n)]
MAX = 0

for i in range(n):
    graph[i] = list( map ( int, input().split() ) )
    MAX = max( max(graph[i]), MAX )

dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

def bfs(x,y,h):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x_, y_ = queue.popleft()
        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
                queue.append((nx, ny))
                visited[nx][ny] = 1

result = 0

for i in range(MAX):
    count = 0
    visited = [ [0] * n for _ in range(n) ]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                count += 1
                
    result = max(result, count)
    
print(result)
