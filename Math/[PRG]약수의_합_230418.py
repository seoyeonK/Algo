def solution(n):
    answer = 0
    if n==0 or n==1:
        answer = n
    elif n==2:
        answer = 3
    else:
        divisor = [1,n]
        for i in range(2,n//2):
            if n%i==0 and i not in divisor:
                if n//i==i:
                    divisor += [i]
                else:
                    divisor += [i, n//i]
        answer = sum(divisor)
    
    
    return answer






def solution(n):    
    return sum([i for i in range(1, n+1) if n % i == 0])