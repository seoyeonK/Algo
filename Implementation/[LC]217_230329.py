# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
nums = [1,2,3,1]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        exist = set()
        for num in nums:
            if num in exist:
                return True
            else:
                exist.add(num)
        return False

#대박
class Solution:
    def containsDuplicate_2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))