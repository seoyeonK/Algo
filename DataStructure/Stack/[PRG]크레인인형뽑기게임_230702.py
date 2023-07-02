#https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    
    basket = []
    
    width = len(board)
    
    for m in moves:
        crane = [ board[x][m-1] for x in range(width) ] 
        
        for i in range(width):
            if crane[i] != 0:
                board[i][m-1] = 0
                
                if not basket or crane[i] != basket[-1]:
                    basket.append(crane[i])
                else:
                    basket.pop(-1)
                    answer += 2
                break
                      
    return answer