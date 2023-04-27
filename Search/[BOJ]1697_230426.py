from collections import deque
N, K = map(int, input().split()) # N ==> K
MAX = 100001
graph = [0]*MAX

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        cur = queue.popleft()
        if cur == K:
            return(graph[cur])
            
        for next in (cur-1, cur+1, cur*2):
            if 0<= next < MAX and not graph[next]:
                graph[next] = graph[cur]+1
                queue.append(next)

print(bfs(N))