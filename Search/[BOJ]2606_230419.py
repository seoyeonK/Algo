from collections import deque
N = int(input())
M = int(input())
com = [[] for n in range(N)]
for m in range(M):
    a,b = map(int,input().split())
    com[a-1].append(b-1)
    com[b-1].append(a-1)

visited = [0]*N

def bfs(node):
    visited[0] = 1
    queue = deque()
    queue.append(node)
    while queue:
        ele = queue.popleft()
        for i in com[ele]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
bfs(0)
print(sum(visited)-1)