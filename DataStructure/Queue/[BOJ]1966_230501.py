from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

result = []
for t in range(T):
    dNum, idx = map(int, input().split())
    docs = list(map(int, input().split()))
    
    queue = deque(docs)
    
    count = 0
    while queue:
        doc = queue.popleft()

        if not queue or doc >= max(queue):  
            count += 1
            if idx == 0 :                   
                result.append(count)
                break
            idx -= 1                         
        else:                               
            queue.append(doc)                
            if idx == 0:                     
                idx = len(queue)-1
            else:                
                idx -= 1

print(*result, sep="\n")