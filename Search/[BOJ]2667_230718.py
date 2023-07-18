from collections import deque
import sys
input = sys.stdin.readline


def bfs(r, c, apt, visited, N):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited[r][c] = True

    queue = deque()
    queue.append((r,c))
    houses = 1  

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and apt[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr,nc))
                houses += 1
    return houses

def solution():
    N = int(input())
    apt = [ [int(x) for x in input().rstrip()] for _ in range(N) ]
    visited = [ [False for _ in range(N)] for _ in range(N) ]

    danji = []

    for i in range(N):
        for j in range(N):
            if apt[i][j] == 1 and not visited[i][j]:
                apts = bfs(i, j, apt, visited, N)
                danji.append(apts)
    
    print(len(danji))
    print(*sorted(danji), sep='\n')

solution()