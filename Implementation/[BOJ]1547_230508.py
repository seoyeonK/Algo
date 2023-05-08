M = int(input())

cups = [1, 0, 0]
for _ in range(M):
    xy = input().rstrip()
    cups[int(xy[0]) - 1], cups[int(xy[2]) - 1] = cups[int(xy[2]) - 1], cups[int(xy[0]) - 1]
print(cups.index(1)+1)