import sys
LN = [0]*26
answer = ''

N = int(sys.stdin.readline())

for _ in range(N) :
    name = sys.stdin.readline().strip()
    LN[ord(name[0])-97] += 1

for i in range(26):
    if LN[i] >= 5:
        answer+=chr(i+97)
if answer == '':
    print("PREDAJA")

print(answer)
