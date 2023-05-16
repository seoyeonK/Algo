T = int(input())

for _ in range(T):
    result = []
    n = int(input())
    binN = []
    idx = 0
    while n > 1:
        binN.append(n%2)
        n = n // 2
    binN.append(n)

    for i in range(len(binN)):
        if binN[i] == 1:
            result.append(i)
    print(*result)
