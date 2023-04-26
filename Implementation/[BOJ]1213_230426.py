import sys
from collections import Counter
name = dict(Counter(sys.stdin.readline().rstrip()))

count = 0
Palin = ''
push = ''

for k in sorted(name.keys()):
    if name[k]%2==1:
        push += k
        count += 1
        if count >= 2:
            print("I'm Sorry Hansoo")
            exit(0)
    if name[k] != 1:
        Palin += k*(name[k]//2)

print(Palin + push + Palin[::-1])