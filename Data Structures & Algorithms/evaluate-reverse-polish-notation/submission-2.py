class Solution:
    def is_valid_number(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            if self.is_valid_number(token):
                operands.append(int(token))
            else: # encountering operator means we have 2 operands
                if token == "+":
                    val = operands.pop() + operands.pop()
                elif token == "-":
                    val = - operands.pop() + operands.pop() # [a,b,-] means a-b, but b gets popped first
                elif token == "*":
                    val = operands.pop() * operands.pop()
                else:
                    val = int(1/operands.pop() * operands.pop())
                
                operands.append(val)
        return operands.pop()
                
                
            