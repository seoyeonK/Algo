from collections import deque

N, M = map(int, input().split())

maze = [ list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(r,c):
    queue = deque()
    queue.append(r, c, 1)

    while queue:
        c_r, c_c, depth = queue.popleft()

        for i in range(4):
            nr = c_r + dy[i]
            nc = c_c + dx[i]

            if 0 <= nr < N and 0 <= nc < M :
                if maze[nr][nc] == 1:
                    if nr == N - 1 and nc == M - 1:
                        return depth + 1
                    else:
                        queue.append((nr, nc, depth + 1))
                        maze[nr][nc] = 0

print(bfs(0,0))