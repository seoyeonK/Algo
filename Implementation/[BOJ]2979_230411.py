import sys
answer = 0

time = [0] * 100
A, B, C = map(int,sys.stdin.readline().split(" "))
for i in range(3):
    s, e = map(int,sys.stdin.readline().split(" "))
    for j in range(s,e):
        time[j] += 1

for t in time:
    if t == 1:
        answer += A
    elif t == 2:
        answer += B*2
    elif t == 3:
        answer += C*3
print(answer)

#wow
a, b, c = map(int, input().split())
arr = [0]*100; answer=0
for _ in range(3):
    begin, end = map(int, input().split())
    for i in range(begin, end): arr[i] += 1
for j in arr:
    answer += {0:0, 1:a, 2:b*2, 3:c*3}[j]
print(answer)

