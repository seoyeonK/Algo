N = int(input())     # 1 ≤ N ≤ 1,000,000

answer = 0

digits = len(list(map(int,str(N)))) 

#N = 9이면
start = N - 9*digits
end = N+1  #10

if start < 0:
    start = N // 2

for gen in range(start,end): # 0 - 9
    if N == gen + sum( list(map(int,str(gen))) ):
        answer = gen
        break

print(answer)

# 시간 줄이기!!
