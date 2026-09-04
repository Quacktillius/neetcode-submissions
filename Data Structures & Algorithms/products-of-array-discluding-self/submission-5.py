class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * (len(nums) + 1)
        for i,n in enumerate(nums):
            pre[i+1] = pre[i] * n
        pre.pop(-1)

        nums.reverse()

        post = [1] * (len(nums) + 1)
        for i,n in enumerate(nums):
            post[-2 - i] = post[-1 - i] * n
        post.pop(0)

        result = []
        for i,j in zip(pre,post):
            result.append(i*j)
        
        return result