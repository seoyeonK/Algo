from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

Dfs = []
visited = [False]*(N+1)
def dfs(x):
    visited[x] = True
    Dfs.append(x)
    for i in sorted(graph[x]):
        if not visited[i]:
            dfs(i)

Bfs = []
def bfs(x):
    queue = deque([x])
    visited[x] = True
     
    while queue:
        ele = queue.popleft()
        Bfs.append(ele)
        
        for i in sorted(graph[ele]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(V)
visited = [False]*(N+1)
bfs(V)

print(*Dfs, sep=" ")
print(*Bfs, sep=" ")