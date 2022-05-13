# https://www.acmicpc.net/problem/10818

import sys 

N = int(sys.stdin.readline())

nums = [int(x) for x in sys.stdin.read().split()]
print(min(nums), max(nums))
# Max = -1000001
# Min = 1000001

# for x in nums:
#     Max = max(Max, x)
#     Min = min(Min, x)

# print( str(Min) + " " + str(Max))
