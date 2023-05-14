import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(r,c):
    garden[r][c] = 0
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if 0 <= nr < N and 0 <= nc < M and garden[nr][nc] == 1:
            DFS(nr,nc)

T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    garden = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        garden[y][x] = 1

    worm = 0
    for r in range(N):
        for c in range(M):
            if garden[r][c] == 1:
                DFS(r,c)
                worm += 1
    print(worm)