import sys
M, N = map(int, sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(M) ]


dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(r, c):
    if r == M-1 and c == N-1:
        return 1

    if dp[r][c] > -1:
        return dp[r][c]

    dp[r][c] = 0
     
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]

        if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] < graph[r][c]:
            dp[r][c] += dfs(nr,nc)
            
    return dp[r][c]

   
print(dfs(0,0))