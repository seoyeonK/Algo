N, K = map(int, input().split())

mul = 1
div = 1

for i in range(N, N-K, -1):
    mul *= i

for j in range(1, K+1):
    div *= j

print(mul//div)