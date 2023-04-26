from collections import deque
import sys
answer = 0

M, N, H = map(int, sys.stdin.readline().split()) # 열 행 높
graph = []

queue = deque()

for h in range(H):
    tmp = []
    for r in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for c in range(M):
            if tmp[r][c] ==1:
                queue.append((h,r,c))
    graph.append(tmp)

dr = [1,-1,0,0,0,0]
dc = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1]

while queue:
    h,r,c = queue.popleft()
    for i in range(6):
        nr = r+dr[i]
        nc = c+dc[i]
        nh = h+dh[i]
        if 0<= nr < N and 0 <= nc < M and 0 <= nh <H and graph[nh][nr][nc] == 0:
            queue.append((nh,nr,nc))
            graph[nh][nr][nc] = graph[h][r][c] + 1
            
    
day = 0
for h in graph:
    for r in h:
        for c in r:
            if c == 0:
                print(-1)
                exit(0)
        day = max(day, max(r))
print(day-1)