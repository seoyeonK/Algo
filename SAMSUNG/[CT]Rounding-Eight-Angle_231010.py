N = 4
arr = [[0] * 8] + [list(map(int, input())) for _ in range(N)]
K = int(input())

top = [0] * (N + 1)

for _ in range(K):
    idx, dir = map(int, input().split()) # dir : cw = 1, ccw = -1 

    tlist = [(idx, 0)]          # when rotating, value of top has to add 1 for ccw, subtract 1 for cw

    for i in range(idx + 1, N + 1):     #look for right side of idx wheeln 
        if arr[i - 1][(top[i - 1] + 2) % 8] != arr[i][(top[i] + 6) % 8]:
            tlist.append((i, (i - idx) % 2))
        else:
            break
    
    for i in range(idx - 1, 0, -1):
        if arr[i][(top[i] + 2) % 8] !=  arr[i + 1][(top[i + 1] + 6) % 8] :
            tlist.append((i, (idx - i) % 2))
        else:
            break
    
    for i, dr in tlist:
        if dr == 0 : 
            top[i] = (top[i] - dir + 8) % 8
        else:
            top[i] = (top[i] + dir + 8) % 8

answer = 0
calc = [0, 1, 2, 4, 8]

for i in range(1, N + 1):
    answer += arr[i][top[i]] * calc[i]

print(answer)