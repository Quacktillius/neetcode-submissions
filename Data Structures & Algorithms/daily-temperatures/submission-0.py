class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        toFind = []
        vals = [0] * len(temperatures)
        for j,t in enumerate(temperatures):
            while len(toFind) > 0 and toFind[-1][1] < t:
                i,tt = toFind.pop()
                vals[i] = j - i
            toFind.append((j,t))
        return vals
        
            