N = int(input())

temp = [[0 for i in range(10)] for i in range(N)]
temp[0] = [1 for i in range(10)]
temp[0][0] = 0


for i in range(1,N):
    for j in range(10):
        if j == 0 :
            temp[i][j] = temp[i-1][j+1]
        elif j == 9:
            temp[i][j] = temp[i-1][j-1]
        else:
            temp[i][j] = temp[i-1][j-1] + temp[i-1][j+1]

print(sum(temp[N-1])%1000000000)