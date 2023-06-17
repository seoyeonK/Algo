def prime(n):
    isPrime = True

    if n == 1 :
        isPrime = False

    else:
        for i in range(2,int(n**1/2)+1):
            if n % i == 0:
                isPrime = False
                break

    return isPrime

N = int(input())

nums = list(map(int, input().split()))

result = 0

for n in nums:
    if prime(n):
        result += 1

print(result)