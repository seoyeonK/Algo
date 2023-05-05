N = int(input())
nums = sorted(list(map(int, input().split())))

M = int(input())
targets = list(map(int, input().split()))

def binarySearch(target, nums):
    start = 0
    end = len(nums) -1

    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for t in targets:
    print(binarySearch(t,nums))
