N = int(input())
num = [int(input()) for x in range(N) ]
print(*sorted(num), sep='\n')