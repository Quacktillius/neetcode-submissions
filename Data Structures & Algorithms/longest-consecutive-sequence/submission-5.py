class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxL = 0
        for n in nums:
            if n-1 in s:
                continue
            l = 1
            while n + 1 in s:
                l += 1
                n += 1
            maxL = max(l, maxL)

        return maxL