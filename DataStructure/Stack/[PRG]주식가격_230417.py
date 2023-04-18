from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        count = 0
        
        for i in prices:
            if i < c:
                count +=1 
                break
            count += 1          
        answer.append(count)


    return answer

# #referenced