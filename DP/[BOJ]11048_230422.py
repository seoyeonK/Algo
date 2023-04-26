import sys
N, M = map(int, sys.stdin.readline().split())  # N행 M열

graph = [0 for _ in range(N+1)]
graph[0] = [0 for _ in range(M+1)]

for n in range(1,N+1):
    graph[n] = [0] + list(map(int,sys.stdin.readline().split()))

dp = [[0 for _ in range(M+1)]for _ in range(N+1) ]
for r in range(1,N+1):
    for c in range(1,M+1):
        dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + graph[r][c]

print(dp[N][M])