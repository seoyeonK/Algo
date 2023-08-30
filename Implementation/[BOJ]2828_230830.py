N, M = map(int, input().split())
J = int(input())
apple = [int(input())-1 for _ in range(J)]
cur = 0
move = 0
for a in apple:
    if a < cur:
        move += cur - a
        cur = a
    elif cur + M <= a:
        move += a - cur - M + 1
        cur = a - M + 1
print(move)