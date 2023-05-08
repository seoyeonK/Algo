import sys

alph = [0]*26
S = sys.stdin.readline().strip()

for s in S:
    alph[ord(s)-97] += 1

print(*alph)