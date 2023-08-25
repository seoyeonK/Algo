# https://school.programmers.co.kr/learn/courses/30/lessons/12939 

def solution(s):
    num = sorted(list(map(int, s.split(" "))))
    
    answer = str(num[0]) + ' ' + str(num[-1])
    
    return answer
