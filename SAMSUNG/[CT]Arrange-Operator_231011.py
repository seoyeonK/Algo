n = int(input())
nums = list(map(int, input().split()))
Add, Sub, Mul = map(int, input().split())   # [add, subtract, mulitiply]

MAX_val = -1000000000
MIN_val = 1000000000

cur = nums[0]

def dfs(cur, next_idx, Add, Sub, Mul):
    global MAX_val, MIN_val, opers
    
    if next_idx == n :
        MAX_val = max(MAX_val, cur)
        MIN_val = min(MIN_val, cur)

    if Add:
        dfs(cur + nums[next_idx], next_idx + 1, Add - 1, Sub, Mul )

    if Sub:
        dfs(cur - nums[next_idx], next_idx + 1, Add, Sub - 1, Mul )

    if Mul:
        dfs(cur * nums[next_idx], next_idx + 1, Add, Sub, Mul - 1 )

dfs(cur, 1, Add, Sub, Mul)

print(MIN_val, MAX_val)