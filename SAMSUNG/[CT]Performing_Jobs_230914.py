# def combinations(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations(arr[i+1:], r-1):
#                 yield [arr[i]] + next
            
# def solution():
#     n = int(input())
#     half = n//2

#     work = [ list(map(int, input().split())) for _ in range(n) ]

#     task = [i for i in range(n)]
#     combo = sorted(list(combinations(task, half)))
    
#     balance = []
    
#     for jobs in combo:
#         intensity = 0
#         intensities = list(combinations(jobs, 2))
        
#         for i, j in intensities:
#             intensity += work[i][j]
#             intensity += work[j][i]
            
#         balance.append(intensity)
        
#     min_diff = abs(balance[0] - balance[-1])
    
#     for i in range(1, len(balance)//2):
#         diff = abs(balance[i] - balance[-i-1])
#         if min_diff > diff : 
#             min_diff = diff
        

#     print(min_diff)

# solution()

# 일의 양 (2의 배수)
n = int(input())

# 업무 간의 상성 Pij
work = [list(map(int, input().split())) for _ in range(n)]

def work_intensity(day):
    res = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            res += work[day[i]][day[j]]
            res += work[day[j]][day[i]]
    return res

def dfs(idx, depth):
    global ans
    if depth == n//2:
        temp2 = [i for i in range(n) if i not in temp]
        ans = min(ans, abs(work_intensity(temp) - work_intensity(temp2)))
        
    for i in range(idx + 1, n): #idx = 0 부터 시작하면 
        temp.append(i)
        dfs(i, depth+1)
        temp.pop()

total = set(range(n))
temp = [0]
ans = float("INT")
dfs(0,1)

print(ans)