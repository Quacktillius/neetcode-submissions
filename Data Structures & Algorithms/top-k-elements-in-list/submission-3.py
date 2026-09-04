class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        sortedList = [ (n,c) for n,c in counter.items()]
        sortedList.sort(key=lambda x : -x[1])

        return list(map(lambda x: x[0], sortedList[0:k]))
