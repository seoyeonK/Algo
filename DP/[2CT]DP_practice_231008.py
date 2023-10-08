# 1로 만들기 

def make_one(x):
    d = [0] * 30000

    for i in range(2, x+1):
        d[i] = d[i-1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5] + 1)

    return d[x]


# 2. 개미전사
def ant_warrior(N, food):
    dp = [0] * N
    dp[0] = food[0]
    dp[1] = max(dp[0], food[1])

    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + food[i])
    
    return dp[N-1]

def money(N, M, coins):
    d = [10001] * (M+1)
    d[0] = 0

    for i in range(N):
        for j in range(coins[i], M+1):
            if d[j - coins[i]] != 10001:
                d[j] = min(d[j], d[j-coins[i] + 1])