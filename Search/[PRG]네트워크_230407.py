n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	

def solution(n, computers):
    answer = 0
    
    
    def dfs(r,c):
        if r < 0 or r >= n or c < 0 or c >= n:
            return 
        if r != c and computers[r][c] == 1:
            computers[r][c] = 0
            dfs(r-1,c)

        
    
    
    return answer