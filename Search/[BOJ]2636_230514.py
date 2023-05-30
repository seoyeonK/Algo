from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int,input().split())

graph = [[] for _ in range(R)]


for r in range(R):
    graph[r] = list(map(int,input().split()))


dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs():
    count = 0

    queue = deque()
    queue.append((0,0))

    visited[0][0] = 1

    while queue:
        cr, cc = queue.popleft()
        
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    count += 1
                else:
                    queue.append((nr,nc))
                
    return count

melt = []
time = 0
while True:
    visited = [[0]*C for _ in range(R)]
    melt.append(bfs())
    if melt[-1] == 0:
        break
    
    time += 1

print(time)
print(melt[-2])