import sys

n = int(sys.stdin.readline())

result = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for i in result:
    print(i)




# import sys  # sys모듈 읽어들이기

# t = int(sys.stdin.readline())

# for _ in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)