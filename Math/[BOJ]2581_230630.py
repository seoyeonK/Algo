M = int(input())
N = int(input())

def isDecimal(x):
    result = True

    if x == 1:
        result = False

    else:
        for i in range(2,int(x**0.5)):
            if x % i == 0:
                result = False
                break
    return result

decimal = [x for x in range(M,N+1) if isDecimal(x)]

if not decimal:
    print(-1)

else:
    print(sum(decimal))
    print(decimal[0])