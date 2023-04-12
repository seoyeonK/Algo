import sys

N, M = map(int, sys.stdin.readline().split(" "))

poke = []
poke.append('')
poke_h = dict()

for idx in range(1,N+1):
    mon = sys.stdin.readline().strip()
    poke.append(mon)
    poke_h[mon] = idx

answer = []
for _ in range(M):
    quiz = sys.stdin.readline().strip()
    if quiz.isalpha():
        answer.append(poke_h[quiz])
    elif quiz.isdigit():
        answer.append(poke[int(quiz)])

print(*answer, sep="\n")