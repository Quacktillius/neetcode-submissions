class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lsf = prices[0]
        maxP = 0
        for i,p in enumerate(prices):
            profit = p - lsf
            maxP = max(maxP, profit)
            lsf = min(lsf, p)
        return maxP
