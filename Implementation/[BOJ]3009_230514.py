X = []
Y = []
for i in range(3):
    x, y = map(int, input().split())
    if x in X:
        X.remove(x)
    else:
        X.append(x)

    if y in Y:
        Y.remove(y)
    else:
        Y.append(y)

print(X[0], Y[0])


X = []
Y = []
for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x = X[0]
y = Y[0]

if X[0] == X[1]:
    x = X[2]
elif X[0] == X[2]:
    x = X[1]
if Y[0] == Y[1]:
    y = Y[2]
elif Y[0] == Y[2]:
    y = Y[1]

print(x,y)