def solution(number, k):
    answer = ''
    nums = sorted(list(set(number)))
    print(nums)
    nums = nums[:k]
    print(nums)                  
    for n in number:
        if n not in nums:
            answer+=n
    return answer

number = "1924"
k = 2

print(solution(number,k))