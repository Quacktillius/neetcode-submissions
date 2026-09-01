class Solution:
        
    def isValid(self, s: str) -> bool:
        stack = []

        brackets_map = {
        '(': ')',
        '[': ']',
        '{': '}'
       }
        
        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            if c == "]" or c == "}" or c == ")":
                if not len(stack) > 0:
                    return False
                latest = stack.pop()
                if not latest in brackets_map or not brackets_map[latest] == c:
                    return False
        if len(stack) == 0:
            return True
        return False
