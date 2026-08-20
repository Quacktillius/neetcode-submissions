class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            t = target - nums[i]
            j = nums.index(t) if t in nums else -1
            if j == i:
                j = nums.index(t, i+1) if t in nums[i+1:] else -1
            if j != -1:
                return [i, j]