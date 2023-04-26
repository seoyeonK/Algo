N = int(input())

temp = [1 for i in range(10)]

for i in range(1,N):
    for j in range(1,10):
        temp[j] += temp[j-1]

print(sum(temp)%10007)