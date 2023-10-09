N = 4

arr = [[0] * 8] + [list(map(int, input())) for _ in range(N)]
K = int(input())

top = [0] * (N+1)

for _ in range(K):
    idx, dr = map(int, input().split())     #dr : cw = 1, ccw = -1 
    tlst = [(idx, 0)]                       # => but when rotating, ccw has to add to top[idx], cw has to subtract
    
    # right side of idx wheel
    for i in range(idx + 1, N + 1):        
        if arr[i-1][(top[i - 1] + 2) % 8] != arr[i][(top[i] + 6) % 8] :
            tlst.append((i, (i - idx) % 2))
        else:
            break
    #left side of idx wheel
    for i in range(idx-1, 0, -1):
        if arr[i][(top[i] + 2) % 8] != arr[i + 1][(top[i+1] + 6) % 8] :
            tlst.append((i, (idx - i)%2 ))
        else:
            break
    
    for i, rot in tlst:
        if rot == 0:    #rotate same direction ( abs(idx - i) % 2 == 0 )
            top[i] = (top[i] - dr + 8) % 8
        else:
            top[i] = (top[i] + dr + 8) % 8
    
answer = 0
calc = [0, 1, 2, 4, 8]

for i in range(1, N+1):
    answer += arr[i][top[i]] * calc[i]

print(answer)