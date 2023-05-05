from collections import deque
import sys
N, M = map(int, sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline())) for _ in range(N)]

ice = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] > 0:
            ice.append((i,j))

def bfs(r,c):
    visited[r][c] = 1
    queue = deque((r,c))
    melt = []
    while queue:
        R, C = queue.popleft()
        sea = 0

        for i in range(4):
            nr = R + dy
            nc = C = dx

            if 0 <= nr < N and 0 <= nc < M :
                if graph[nr][nc] == 0:
                    sea += 1
                elif graph[nr][nc] and not visited[nr][nr]:
                    queue.append((nr,nc))
                    visited[nr][nc] = 1
        if sea > 0:
            melt.append((R,C,sea))
    for r, c, sea in melt:
        graph[r][c] = max(0, graph[r][c] - sea)
    
    return 1
            
year = 0

while ice:
    visited = [[0] * M for _ in range(N)]
    delList = []
    group = 0

    for i , j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i,j)
        if graph[i][j] == 0:
            delList.append((i,j))
    
    if group > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)


