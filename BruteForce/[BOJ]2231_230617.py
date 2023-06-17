N = int(input())

answer = 0

digits = len(list(map(int,str(N))))


for i in range(N//2, N-1):
    gen = i
    if N == gen + sum( list(map(int,str(gen))) ):
        answer = gen
        break

print(answer)

# 시간 줄이기
