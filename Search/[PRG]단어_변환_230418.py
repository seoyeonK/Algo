from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    queue = deque()
    
    queue.append((begin,0))
    
    while queue:
        word, depth = queue.popleft()
        for w in words:
            if compare(word, w):
                 if w == target:
                    return depth+1
                 else:
                    queue.append((w,depth+1))
                 
    
    
    return answer




def compare(A, B):
    diff = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            diff += 1
    if diff == 1:
        return True
    return False