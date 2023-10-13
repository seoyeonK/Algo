def solution(n):
    answer = [ [0]*n for _ in range(n)]
    
    direct = 0 
    r, c = 0, -1
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    val = 1
    
    while val <= n*n :
        nr, nc = r + dr[direct], c + dc[direct]
            
        if 0 <= nr < n and 0 <= nc < n and answer[nr][nc] == 0:  
            answer[nr][nc] = val 
            r, c = nr, nc
            val += 1
            
        else:
            direct = (direct + 1) % 4
            
    return answer

print(*solution(4), sep='\n')