from collections import deque
n, L, R = map(int, input().split())
eggs = [ list(map(int, input().split())) for _ in range(n)]
answer = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    group = [(r,c)]
    queue = deque()
    queue.append((r,c))
    
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if L <= abs(eggs[nr][nc] - eggs[cr][cc]) <= R: 
                    visited[nr][nc] = True
                    group.append((nr, nc))
                    queue.append((nr, nc))
    return group 

while True:
    # find groups that have L < diff < R
    stop = True
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:                
                visited[i][j] = True
                group = bfs(i, j)
                
                if len(group) > 1:
                    stop = False
                    egg = sum([eggs[r][c] for r,c in group]) // len(group)
                    for r, c in group:
                        eggs[r][c] = egg
    if stop:
        break
  
    answer += 1
    
print(answer)                    
