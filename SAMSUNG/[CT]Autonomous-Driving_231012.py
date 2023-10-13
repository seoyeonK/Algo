n, m = map(int, input().split()) #  n = height, m = width
x, y, d = map(int, input().split())                             # d = 0 ~ 3 : N E S W
roads = [ list(map(int, input().split())) for _ in range(n)]    # 0 : road, 1: sidewalk
visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def can_move(x, y):
    move = False 
    if  0 <= x < n and 0 <= y < m and roads[x][y] == 0 and not visited[x][y]:
        move = True
    return move

visited[x][y] = 1
trial = 0
while True:
    d = (d + 3) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    trial += 1
    
    if can_move(nx, ny): # if can move, (in range, is a road, not visited),  move (change x, y, reset trial, change visited)#  
        x, y = nx, ny
        trial = 0
        visited[x][y] = 1
        
    else:   # if can't move, (already visited, out of range)
        if trial == 4 :     #   if trial == 4 
            nx = x - dx[d]
            ny = y - dy[d]            
            if 0 <= nx < n and 0 <= ny < m and roads[nx][ny] == 0:  #if can go backwards, go backwards(change x, y, reset trial)
                x = nx
                y = ny
                visited[x][y] = 1
                trial = 0                
            else:       # if can't move backwards, (already visited, out of range)
                break
    
        else:       # if trial <4 
            continue

answer = 0
for i in range(n):
    for j in range(m):
        answer += visited[i][j]
print(answer)