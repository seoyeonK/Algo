# # 주어진 금액 만드는 모든 방법
# # input : 
# # 테케 개수 T  (1<= T <= 10)
# # 테케 첫줄 : 동전의 가지 수 N (1<= N <=20)
# # 테케 두번째 줄 : N가지 동전의 각 금액이 오름차순으로 
# # 테케 세번째 줄 : 금액 M  (1<= M <= 10000)

import sys

def func_coin(coins, M):
    dM = [0] * (M+1)
    dM[0] = 1

    for coin in coins:
        for m in range(coin,M+1):
            dM[m] += dM[m-coin]
    return dM[M]

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split(" ")))
    M = int(sys.stdin.readline())

    print(func_coin(coins,M))
    