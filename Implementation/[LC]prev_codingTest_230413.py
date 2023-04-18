def balancedSum(arr):
    lsum = arr[0]
    pivot = 1
    rsum = sum(arr) - lsum - arr[pivot]
    for i in range(pivot,len(arr)-2):
        if rsum == lsum :
            return pivot
        lsum = + arr[pivot]
        rsum -= arr[pivot+1]
        pivot += 1
    return pivot


def squares(queries):
    total = []
    for q in queries:
        r = q[0]
        c = q[1]
        if r > c :
            r,c = c,r
        count = int( r*(r+1)*(2*r+1)/6 + (c-r)*r*(r+1)/2   )
    total.append(count)
    return total
    

def findLIS(nums):
    n = len(nums)
    rst = [1] *n
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                rst[i] = max(rst[i], rst[j]+1)
    return max(rst)

def binarySearch(arr, start, end, target):
    if start <= end :
        mid = start + (end-start)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return binarySearch(arr, (mid+1), end, target)
        else:
            return binarySearch(arr, start, (mid-1), target)
    return -1


def countPais(nums,k):
    num = sorted(list(set(nums)))
    count = 0
    for i in range(0, len(num)):
        target = num[i] + k
        if binarySearch(nums,0,len(nums)-1,target) != -1:
            count +=1
    return count