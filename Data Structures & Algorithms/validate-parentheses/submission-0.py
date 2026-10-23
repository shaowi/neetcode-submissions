class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
             ']': '[',
             '}': '{',
             ')': '('
        }
        stack = []

        for c in s:
            if not c in close_to_open:
                stack.append(c)
                continue
            if not stack or stack[-1] != close_to_open[c]:
                return False 
            stack.pop()                

        return not stack 