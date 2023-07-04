N, K = map(int, input().split())
temp = list(map(int, input().split()))

sum = Max = sum(temp[:K])

for i in range(N-K):
    sum = sum - temp[i] + temp[i+K]

    if Max < sum:
        Max = sum

print(Max)