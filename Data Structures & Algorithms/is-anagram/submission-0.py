class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount_s = {}
        charCount_t = {}

        for c in s:
            if c in charCount_s:
                charCount_s[c] += 1
            else:
                charCount_s[c] = 1
        
        for c in t:
            if c in charCount_t:
                charCount_t[c] += 1
            else:
                charCount_t[c] = 1
        
        return charCount_s == charCount_t