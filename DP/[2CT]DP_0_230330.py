#1 fibonacci -> O(2^N) : n이 커질수록 수행시간이 기하급수적으로 늘어남

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# print(fib(4))


#2 fibonacci -> DP - Top-Down ; recursion
d = [0] * 100       #list for memoization

def fibo_DP1(n) : 
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo_DP1(n-1) + fibo_DP1(n-2)
    return d[n]

#3 fibonacci -> DP - Bottom-up ; loop

def fibo_DP2(n) :
    d = [0] * 100
    d[1] = 1
    d[2] = 1
    for i in range(3,100):
        d[i] = d[i-1] + d[i-2]
    
    return d[n]