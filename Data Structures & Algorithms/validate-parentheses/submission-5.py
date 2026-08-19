class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}" : "{", "]" : "[", ")" : "("}
        stack = []   #the end of the list is the top of the stack
        for i in range(len(s)):
            if s[i] not in map:
                stack.append(s[i])
            else:
                if not stack or map[s[i]] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack