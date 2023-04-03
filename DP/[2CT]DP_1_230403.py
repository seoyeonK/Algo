
#1. 1로 만들기

import sys
def make_one(X):
    dx = [0]*(X+1)

    dx[1] = 0
    dx[2] = 1

    for i in range(3,X+1):
        dx[i] = dx[i-1] + 1

        if i % 5 == 0:
            dx[i] = min(dx[i//5]+1,dx[i])
        if i % 3 == 0:
            dx[i] = min(dx[i//3]+1, dx[i])
        if i % 2 == 0:
            dx[i] == min(dx[i//2]+1, dx[i])
    
    return dx[X]

# print(make_one(26))


#2. 개미전사

def ant_warrior(N:int, food:list[int]) -> int:
    getFood = [0]*N     # i번째 칸을 털었을 때 식량의 최댓값

    getFood[0] = food[0]

    getFood[1] = max(food[0], food[1])

    for i in range(2,N):
        getFood[i] = max(getFood[i-1], food[i] + getFood[i-2])
    
    return getFood[N-1]

# print(ant_warrior(4,[1,3,1,5]))



#3. 바닥 공사


def floor(N):
    d = [0] * (N+1)
    d[1] = 1
    d[2] = 3

    for i in range(3,N+1):
        d[i] = d[i-1] + 2*d[i-2] 
    
    return d[N] % 796796

# print(floor(3))




#4. 효율적인 화폐 구성
def eff_money(N, M, coins):
    d = [10001] * (M+1)    
    d[0] = 0

    for c in coins:
        for i in range(c,M+1):
            if d[i-c] != -1:
                d[i] = min(d[i], d[i-c] + 1)

    if d[M] == 10001:
        return -1
    return d[M]

print(eff_money(2, 15, [2,3]))
#print(eff_money(3, 4, [3,5,7]))    