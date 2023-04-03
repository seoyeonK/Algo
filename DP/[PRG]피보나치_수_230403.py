def solution(n):
    answer = 0

    fib = [0]*(n+1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    
    answer = fib[n]

    return answer

print(solution(5))


def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b, a+b
    return a
