S = input().rstrip()

alph = [-1] * 26

for i in range(len(S)):
    idx = ord(S[i]) - 97
    if alph[idx] == -1:
        alph[idx] = i

print(*alph, sep=' ')