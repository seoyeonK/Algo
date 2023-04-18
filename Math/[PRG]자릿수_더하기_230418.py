def solution(n):
    answer = 0
    while n>=10:
        answer += n%10
        n = n//10
    return answer+n

def solution(n):
    answer = sum(map(int,list(str(n))))
    return answer