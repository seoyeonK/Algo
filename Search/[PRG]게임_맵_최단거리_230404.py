from collections import deque

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

def solutions(maps):
    answer = 0
    #
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    N = len(maps)
    M = len(maps[0])

    def bfs(r,c):
        queue = deque()
        queue.append((r,c))

        while queue:
            r, c = queue.popleft()

            for i in range(4):  #하상우좌
                nr = r + dr[i]
                nc = c + dc[i]

                if nr == 0 and nc == 0:
                    continue
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if maps[nr][nc] == 0:
                    continue

                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr,nc))
    
    bfs(0,0)
    
    answer = maps[N-1][M-1]
    if answer < N+M-2:
        answer = -1
    
    return answer

print(solutions(maps))
