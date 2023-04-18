def makeone():
    X = int(input())

    d = [0]*30001

    for i in range(2, X+1):
        d[i] = d[i-1] + 1
        if i%2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i%5==0:
            d[i] = min(d[i], d[i//5]+1)

    print(d[X-1])

def antwarrior():
    N = int(input())
    foods = list(map(int, input().split()))

    get = [0]*N
    get[0] = foods[0]
    get[1] = max(foods[0], foods[1])
    for i in range(2, N):
        get[i] = max(get[i-2]+foods[i], get[i-1])
    print(get[N-1])


def floor():
    N = int(input())
    d = [0]*(N+1)
    d[1] = 1
    d[2] = 3
    for i in range(3,N+1):
        d[i] = (d[i-1] + 2*d[i-2]) % 796796
    print(d[N])

    

def coins():
    N,M = map(int, input().split())
    given = [int(input()) for i in range(N)]
    d = [10001]*(M+1)
    d[0] = 0
    for i in range(N):
        for j in range(given[i],M+1):
            if d[j-given[i]] != 10001: 
                d[j] = min(d[j], d[j-given[i]]+1)