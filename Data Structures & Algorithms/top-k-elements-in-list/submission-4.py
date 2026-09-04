import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        sortedByCount = []
        for n in set(nums):
            heapq.heappush(sortedByCount, (-counts[n], n))
        result = []
        for i in range(k):
            result.append(heapq.heappop(sortedByCount)[1])
        
        return result
