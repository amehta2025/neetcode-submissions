class Solution: #genuinely not that bad
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(a+b)
            elif s == "-":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(b-a)
            elif s == "*":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(a*b)
            elif s == "/":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(b/a)
            else:
                stack.append(s)
        
        return int(stack[0])