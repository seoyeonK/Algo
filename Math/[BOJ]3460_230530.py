T = int(input())

for t in range(T):
    n = int(input())

    bin = ''

    while n > 1:
        bin += str(n % 2)
        n = n // 2
    bin = (bin + str(n))

    result = []
    
    for i in range(len(bin)):
        if bin[i] == '1':
            result.append(i)
    print(*result, sep=" ")