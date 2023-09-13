n = int(input())

T = []
P = []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (n+1)

for i in range(n):
    for j in range(i+T[i], n+1):
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]
            
print(dp[-1])