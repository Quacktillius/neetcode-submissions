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
            j = i
            while s[j] != self.delim:
                j += 1
            l = int(s[i:j])
            string = s[j+1 : j+l+1]
            arr.append(string)
            i = j + l + 1
        return arr