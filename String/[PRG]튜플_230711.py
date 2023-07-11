def solution(s):
    s = s[2:-2]
    ls = [ list(map(int,x.split(','))) for x in s.split('},{') ]
    ls = sorted(ls, key = lambda x: len(x))
    
    answer = []
    
    for e in ls:
        for num in e:
            if num not in answer:
                answer.append(num)
    
    return answer