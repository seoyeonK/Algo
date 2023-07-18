def solution():
    answer = ''
    S = input().rstrip().upper()

    alph = [0] * 26

    for s in S:
        alph[ord(s)-65] += 1

    M = max(alph)

    if alph.count(M) > 1:
        answer = '?'
    else:
        answer = chr(alph.index(M) + 65)
    
    print(answer)
    return

solution()