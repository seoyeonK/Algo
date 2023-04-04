# 2 <= len(numbers) <= 20,    1 <= each_num <= 50
# 1 <= target <= 1000
numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers:list[int], target:int):
    answer = 0
    
    def target_num(idx, sum):        
        if idx == len(numbers) and sum == target :
            nonlocal answer 
            answer +=1
            return
                
        if idx < len(numbers) :
            target_num(idx+1, sum+numbers[idx])
            target_num(idx+1, sum-numbers[idx])
        

    target_num(0,0)
    return answer

print(solution(numbers,target))
# 코드 구조 - nonlocal answer 때문에 시간 지체
# + 원소 index 처리 때문에 계속 계산이 안됨, 블로그 참고함



from collections import deque
def solution_bfs_queue(numbers,target):
    # 방문한/pop한 원소 temp가 방문할 수 있는 값은 temp의 다음 인덱스에 위치한 numbers원소를 +/-한 값
    # 따라서 index값도 같이 queue에 넣어주는 것이 편리하다
    # 이와 같은 방법에서 bfs인지 dfs인지는 중요하지 않음, index값에 따라 다음 원소를 결정하기 때문
    # 따라서 deque 대신 그냥 list를 사용하고 popleft() 대신 pop()를 하는 stack을 사용하면 오히려 빠름!
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])     #첫번째 원소와 index 삽입
    queue.append([-1*numbers[0],0])  #첫번째 원소*(-1)
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


def solution_dfs_stack(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


#레전드 코드
def solution_1(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else :
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


#2번째 레전드....
from itertools import product
def solution2(numbers, target):
    l = [(x,-x) for x in numbers]
    s = list(map(sum, product(*l))) # l안의 원소들을 하나씩 풀어야 product가 가능해짐

    return s.count(target)