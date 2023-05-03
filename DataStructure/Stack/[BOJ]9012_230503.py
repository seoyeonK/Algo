import sys
T = int(sys.stdin.readline())

result = []
for _ in range(T):
    PS = list(sys.stdin.readline().strip())
    stack = []
    for x in PS :
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:
                stack.pop(-1)
            else:
                stack.append(x)
                break
    if len(stack) > 0:
        result.append("NO")
    else:
        result.append("YES")
print(*result, sep="\n")