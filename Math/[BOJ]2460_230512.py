cur = 0
M = 0
for i in range(10):
    on, off = map(int, input().split())
    cur = cur - on + off
    M = max(M, cur)
print(M)