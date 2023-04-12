import sys

N = int(sys.stdin.readline())
answer = 0
for _ in range(N) : 
    word = sys.stdin.readline().strip()
    stack = []

    for i in range(len(word)):
        if stack and word[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[i])
    
    if not stack:
        answer += 1
print(answer)
