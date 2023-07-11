N = int(input())

def fibo(N):
    fib = [0] * (N+1)
    if N >= 1 :
        fib[1] = 1
        for i in range(2,N+1):
            fib[i] = fib[i-1] + fib[i-2]
    
    return fib[N]

print(fibo(N))    