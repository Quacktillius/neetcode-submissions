class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            if str(sorted(s)) in result:
                result[str(sorted(s))].append(s)
            else:
                result[str(sorted(s))] = [s]
        return [ v for k,v in result.items()]