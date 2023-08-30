from collections import deque

def bfs(ripe, box, N, M):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    queue = deque() 
    for x,y in ripe:
        queue.append((x,y))

    day = 0
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M :
                if box[nr][nc] == 0 :
                    box[nr][nc] = box[r][c] + 1
                    queue.append((nr,nc))
                    
                    if day < box[nr][nc]:
                        day = box[nr][nc]
    return day


def solution():
    M, N = map(int, input().split())
    box = []
    ripe = []

    for n in range(N):
        tom = list(map(int, input().split()))
        box.append(tom)

        for m in range(M):
            if tom[m] == 1:
                ripe.append((n,m))


    day = bfs(ripe, box, N, M)

    for n in range(N):
        if 0 in box[n]:
            day = -1
            break

    if day > 0 :
        day -= 1

    print(day)

solution()