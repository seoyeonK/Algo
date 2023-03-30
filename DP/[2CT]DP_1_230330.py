# 1. 1로 만들기

# 정답

def make_one(x):
    d = [0] * 30000    # max of x is 30000

    for i in range(2,x+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3]+1)  
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)
    return d[x]



# 2. 개미전사 - pg.220
#   3<= N <=100
#   0<= K <= 1000
N = 4
food = [1,3,1,5]

def ant_warrior(N:int, food:list[int]) -> int:
    dp = [0]*N
    dp[0] = food[0]
    dp[1] = max(food[0], food[1])
    
    for i in range(2,N):
        dp[i] = max(dp[i-1], dp[i-2]+food[i])
    
    return dp[N-1]

# print(ant_warrior(N,food))



# 3. 바닥공사
# N x 2  =>  1x2 , 2x1, 2x2

#정답

def floor(N:int)->int:
    d = [0] * 1001

    d[1] = 1    # 1x2 => 1 가지
    d[2] = 3    # 2x1*2 + 1x2 / 1x2 + 2x1*2 / 2x2 => 3가지

    # N-1에서 1짜리 만들기 => 1x2짜리 1가지
    # N-2에서 2짜리 만들기 => 2x1 2개 / 2x2 1개 => 2가지 

    for i in range(3, N+1):
        d[i] = (d[i-1] + 2*d[i-2]) % 796796

    return d[N]

    
# print(floor(3))



# 4. 효율적인 화폐 구성
# N가지 화폐 => 최소한의 개수로 M원 만들기 

def money(N:int, M:int, coins:list[int])-> int:
    d = [10001] * (M+1)
    d[0] = 0

    for i in range(N):
        for j in range(coins[i],M+1):
            if d[j-coins[i]] != 10001 :     # (i-k)원을 만드는 방법이 존재하는 경우
                d[j] = min(d[j], d[j-coins[i]]+1)
 
    return d[M]


gold = [1,3,3,2,2,1,4,1,0,6,4,7]

