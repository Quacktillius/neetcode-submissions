class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            half = target - nums[i]
            if half in nums[i+1:]:
                return [i, nums[i+1:].index(half) + i + 1]
            