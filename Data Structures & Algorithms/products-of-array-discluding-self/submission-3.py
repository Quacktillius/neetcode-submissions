class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pref = [0] * l
        suff = [0] * l
        for i,n in enumerate(nums):
            j = l-1-i
            if i == 0:
                pref[i] = 1
                suff[j] = 1
            else:
                pref[i] = pref[i-1] * nums[i-1]
                suff[j] = suff[j+1] * nums[j+1]
        
        arr = [0] * l
        for i in range(len(pref)):
            arr[i] = pref[i] * suff[i]
        
        return arr
            
        