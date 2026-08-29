class Solution:
    delim = ';'

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = len(s)
            encoded += str(l) + self.delim + s
        return encoded

    def decode(self, s: str) -> List[str]:
        arr = []
        total_len = len(s)
        i = 0
        while i < total_len:
            l = ""
            while s[i] != self.delim:
                l += s[i]
                i += 1
            l = int(l)
            string = s[i+1 : i+l+1]
            arr.append(string)
            i += l + 1
        return arr