w, h = map(int,input().split())
num = int(input())

X = [0,w]
Y = [0,h]
for _ in range(num):
    x, y = map(int, input().split())
    if x == 0:
        Y.append(y)
    else:
        X.append(y)

X.sort()
Y.sort()

wid = []
hei = []

for i in range(len(X)-1):
    wid.append(X[i+1]-X[i])

for i in range(len(Y)-1):
    hei.append(Y[i+1]-Y[i])

wid = sorted(list(set(wid)))
hei = sorted(list(set(hei)))

print(wid[-1]*hei[-1])