class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first decide row
        l,r = 0, len(matrix)
        while l < r:
            m = l + (r-l)//2
            if target == matrix[m][0]:
                return True
            elif target < matrix[m][0]:
                r = m
                continue
            else:
                l = m + 1
                continue
        if matrix[m][0] < target:
            i = m
        else:
            i = m-1

        l,r = 0, len(matrix[i])
        while l<r:
            m = l + (r-l)//2
            if target == matrix[i][m]:
                return True
            elif target < matrix[i][m]:
                r = m
                continue
            else:
                l = m + 1
                continue
        return False

