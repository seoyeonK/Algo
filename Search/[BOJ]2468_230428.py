import sys
sys.setrecursionlimit(100000)


n = int(input())

graph = [ [] for _ in range(n)]
MAX = 0

for i in range(n):
    graph[i] = list( map ( int, input().split() ) )
    MAX = max( max(graph[i]), MAX )

dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

def dfs(x,y,h):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
            dfs(nx,ny,h)

result = 0

for i in range(MAX):
    count = 0
    visited = [ [0] * n for _ in range(n) ]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                dfs(j, k, i)
                count += 1
                
    result = max(result, count)
    
print(result)