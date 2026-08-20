class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        return list(map( lambda x: x[0] , sorted(list(freq.items()), key=lambda f: -f[1])[:k]))

