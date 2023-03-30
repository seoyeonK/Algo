# 주어진 금액 만드는 모든 방법
# input : 
# 테케 개수 T  (1<= T <= 10)
# 테케 첫줄 : 동전의 가지 수 N (1<= N <=20)
# 테케 두번째 줄 : N가지 동전의 각 금액이 오름차순으로 
# 테케 세번째 줄 : 금액 M  (1<= M <= 10000)

# input : 
#     3
#     2
#     1 2
#     1000
#     3
#     1 5 10
#     100
#     2
#     5 7
#     22

#output :
    # 501
    # 121
    # 1


#https://d-cron.tistory.com/23

# # 1) 2차원 DP table 코드
# import sys
# T = int(sys.stdin.readline())   # num of cases

# for _ in range(T):
#     N = int(sys.stdin.readline())  # N개의 coin
#     coins = list(map(int, sys.stdin.readline().split()))
#     coins.insert(0,0)
#     M = int(sys.stdin.readline())  #target 

#     dp = [[0]*(M+1) for i in range(N+1)]  # 표 생성 
#     for i in range(N+1) :
#         dp[i][0] = 1                        #어느 코인이든 0원을 만드는 가지수 = 0 

#     for j in range(1,N+1):  #coin 개수만큼 차례대로
#         for i in range(1, M+1):     # M원까지 각 coin별 가지수 차례대로 계산
#             dp[j][i] = dp[j-1][i]   # coins[j]원짜리 coin으로 i원을 만드는 가지수는 j-1번째까지 coin들로 i원을 만드는 가지수
#             if i-coins[j] >= 0 :
#                 dp[j][i] += dp[j][i-coins[j]]  #j번째 coin으로 i원 만드는 가지수는 j번째 coin으로만 i원 만드는 가지수에 i-(j번째coin)원 만드는 가지수를 더함
#     print(dp[N][M])

# 2) 1차원 DP table 코드
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins :
        for i in range(1, M+1):
            if i >= coin :
                dp[i] += dp[i-coin]