class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = [c.lower() if c.isalnum() else '' for c in s]
        s = ''.join(stripped)
        stripped.reverse()
        r = ''.join(stripped)
        return s == r