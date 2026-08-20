class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        # Steps:
        # 1. get list of freq items [(1,1), (2,2), (3,3)]
        # 2. sort list by the -count (index 1) (sorting by negative brings largest to the lower indices)
        # 3. grab first k in that sorted list (x,y)
        # 4. map above list by grab the number itself (not count) (index 0)
        # 5. return
        return list(map( lambda x: x[0] , sorted(list(freq.items()), key=lambda f: -f[1])[:k]))

