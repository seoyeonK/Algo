from collections import deque
import sys 
input = sys.stdin.readline
M, N = map(int, input().split())

toma = [[] for _ in range(N)]
ripe = []
for n in range(N):
    toma[n] = list(map(int, input().split()))
    for m in range(M):
        if toma[n][m] == 1:
            ripe.append((n,m))

def bfs(ripe):  
    queue = deque()

    for x,y in ripe:
        queue.append((x,y))

    day = 0

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if toma[nr][nc] == 0:
                    toma[nr][nc] = toma[r][c] + 1
                    queue.append((nr,nc))
                    
                    temp = toma[nr][nc]
                    if day < temp:
                        day = temp
    return day

day = bfs(ripe)

for n in range(N):
    for m in range(M):
        if toma[n][m] == 0:
            day = -1
            break
if day > 0:
    day -= 1

print(day)