class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        stack = []
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if pairs[c] != curr:
                    return False
        
        return len(stack) == 0
