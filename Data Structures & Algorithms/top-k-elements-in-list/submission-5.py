class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        for n,c in counts.items():
            bucket[c].append(n)

        result = []
        kk = 0

        while len(result) < k:
            commonest = bucket[-1 - kk]
            if len(commonest) > 0:
                result += commonest
            kk += 1
        return result
            