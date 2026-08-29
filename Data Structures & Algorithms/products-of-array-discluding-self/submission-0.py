class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            if n != 0:
                product *= n

        zeros = []
        for i,n in enumerate(nums):
            if n == 0:
                zeros.append(i)

        answer = []
        product_is_zero = len(zeros) > 0
        more_than_1_zero = len(zeros) > 1
        for n in nums:
            if product_is_zero:
                if more_than_1_zero:
                    answer.append(0)
                else:
                    if n == 0:
                        answer.append(product)
                    else:
                        answer.append(0)
            else:
                answer.append(int(product / n))
        
        return answer
        