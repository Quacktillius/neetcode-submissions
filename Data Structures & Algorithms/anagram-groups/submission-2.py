class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorteds = {}
        for s in strs:
            ss = ''.join(sorted(s))
            sorteds[ss] = sorteds.get(ss, []) + [s]
        return list(sorteds.values())