# n = int(input())

# dp = [0]*(n+1)

# dp[1] = 1
# dp[2] = 3

# if n>2:
#     for i in range(3,n+1):
#         dp[i] = (dp[i-1] + 2*dp[i-2])%10007

# print(dp[n])
import sys
sys.setrecursionlimit(10000000)

n = int(input())
d = {1:1, 2:3}
def calc(x):
    if x in d.keys():
        return d[x]
    d[x] = (calc(x-1) + 2*(calc(x-2)))%10007
    return d[x]

print(calc(n))