import sys

N, K = map(int, sys.stdin.readline().split(" "))

temp = list(map(int, sys.stdin.readline().split(" ")))

max = 0

for i in range(K):
    max += temp[i]
sum = max
for i in range(N-K):
    sum = sum - temp[i] + temp[i+K]
    if sum > max:
        max = sum
print(max)