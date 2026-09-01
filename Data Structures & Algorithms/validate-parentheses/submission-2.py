class Solution:
    def matches(self, a: str, b: str) -> bool:
        combine = a + b
        match combine:
            case "()" | "{}" | "[]":
                return True
        return False
        
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            if c == "]" or c == "}" or c == ")":
                if not len(stack) > 0:
                    return False
                latest = stack.pop()
                if not self.matches(latest, c):
                    return False
        if len(stack) == 0:
            return True
        return False
