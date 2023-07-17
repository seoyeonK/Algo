import sys
from collections import deque

input = sys.stdin.readline

def bfs(i, j, heights, visited, N, rain):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    visited[i][j] = True

    queue = deque()
    queue.append((i,j))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and heights[nr][nc] > rain:
                visited[nr][nc] = True
                queue.append((nr,nc))


def solution():
    N = int(input())
    heights = []
    Max_height = 0
    for _ in range(N):
        row = list(map(int, input().split()))
        heights.append(row)
        Max_height = max(Max_height, max(row))

    safe_zone = []

    for rain in range(1,Max_height):
        visited = [ [False for _ in range(N)] for _ in range(N) ]
        zones = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and heights[i][j] > rain:
                    bfs(i,j, heights, visited, N, rain)
                    zones += 1
        safe_zone.append(zones)

    if not safe_zone:
        print(1)
    else:
        print(max(safe_zone))
    return

solution()