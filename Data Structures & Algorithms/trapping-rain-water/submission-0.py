from collections import defaultdict
class Solution:
    def trap(self, height: List[int]) -> int:
        leftW = [0] * (len(height) + 1)
        for i,h in enumerate(height):
            leftW[i+1] = max(h,leftW[i])
        leftW.pop(-1)
        # print(leftW)

        height.reverse()

        rightW = [0] * (len(height) + 1)
        for i,h in enumerate(height):
            rightW[i+1] = max(h,rightW[i])
        rightW.pop(-1)
        rightW.reverse()
        # print(rightW)

        height.reverse()

        summation = 0
        for i,h in enumerate(height):
            waterAti = min(leftW[i], rightW[i]) - h
            summation += waterAti if waterAti > 0 else 0
        
        return summation