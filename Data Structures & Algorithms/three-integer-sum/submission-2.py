class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        # print('\t2Sum:', nums, target)
        l, r = 0, len(nums) - 1
        result = []
        while l < r:
            if nums[l] + nums[r] == target:
                result.append([nums[l], nums[r]])
                r -= 1
            if nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return result


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i,n in enumerate(nums):
            sub = nums[i+1:]

            target = -n
            # print('3Sum:', n, sub, target)
            ans = self.twoSum(sub, target)
            if ans != None:
                for an in ans:
                    result.add(tuple([n] + an))
        return [list(t) for t in result]
