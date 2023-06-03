import sys
input = sys.stdin.readline

alph = [ chr(x) for x in range(97,123) ]

name = {x:0 for x in alph}

N = int(input())
for n in range(N):
    first = input().rstrip()[0]
    name[first] += 1

result = ''
for x in alph:
    if name[x] >= 5:
        result += x

if not result:
    result = "PREDAJA"

print(result)
