# N = int(input())
# dp = [0]*(N+1)

# for i in range(2,N+1):
#     dp[i] = dp[i-1] + 1
#     if i%2 == 0:
#         dp[i] = min(dp[i], dp[i//2]+1)
#     if i%3 == 0:
#         dp[i] = min(dp[i], dp[i//3]+1)

# print(dp[N])



# REF
import sys
d = {1: 0, 2: 1}
def s(n: int) -> int:
    if n in d:
        return d[n]
    
    d[n] = 1 + min(s(n // 3) + n % 3, s(n // 2) + n % 2)
    return d[n]
print(s(int(sys.stdin.readline())))