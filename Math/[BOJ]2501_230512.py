N, K = map(int, input().split())
res = 0
div = []
for i in range(1, N//2+1):
    if N%i == 0:
        div += [i, N//i]
        if i == N//i :
            break
div = sorted(set(div))
if K <= len(div):
    res = div[K-1]
print(res)