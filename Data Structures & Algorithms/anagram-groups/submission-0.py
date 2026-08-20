class Solution:
    def isAnagrams(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = [0] * 26
        for i in range(len(s)):
            charCount[ord(s[i]) - ord('a')] += 1
            charCount[ord(t[i]) - ord('a')] -= 1
        
        for c in charCount:
            if c != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorteds = {}
        for s in strs:
            ss = ''.join(sorted(s))
            sorteds[ss] = sorteds.get(ss, []) + [s]
        ans = []
        for k,v in sorteds.items():
            ans += [v]
        return ans