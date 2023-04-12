import sys

M = int(sys.stdin.readline())

cups = [1,0,0]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split(" "))
    if a==b:
        continue
    cups[a-1],cups[b-1] = cups[b-1],cups[a-1]
    

for i in range(3):
    if cups[i] == 1:
        print(i+1)

# print(cups.index(1))