def look_around(r, c, favorites):
    fav, blanks = 0, 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < n and 0 <= nc < n:
            if ride[nr][nc] in favorites:
                fav += 1
            elif ride[nr][nc] == 0:
                blanks += 1
    return fav, blanks
        
n = int(input())
like_info = [ list(map(int, input().split())) for _ in range(n*n) ]

ride = [ [0]*(n) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(n * n):
    student = like_info[i][0]
    favorites = like_info[i][1:]
    
    candidates = []
    
    for r in range(n):
        for c in range(n):
            
            if ride[r][c] == 0:
                fav, blanks = look_around(r, c, favorites)
                candidates.append([fav, blanks, r, c])
                
    candidates.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))
    seat = candidates[0]
    ride[seat[2]][seat[3]] = student

students = [x[0] for x in like_info]

answer = 0
for i in range(n):
    for j in range(n):
        student_idx = students.index(ride[i][j])
        fav, blanks = look_around(i, j, like_info[student_idx][1:])
        if fav > 0:
            answer += 10 ** (fav - 1)
print(answer)
        