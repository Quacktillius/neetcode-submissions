class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            if n != 0:
                product *= n

        count_zeros = 0
        for i,n in enumerate(nums):
            if n == 0:
                count_zeros += 1

        answer = []
        for n in nums:
            if count_zeros > 0:
                if count_zeros > 1:
                    answer.append(0)
                else:
                    if n == 0:
                        answer.append(product)
                    else:
                        answer.append(0)
            else:
                answer.append(int(product / n))
        
        return answer
        