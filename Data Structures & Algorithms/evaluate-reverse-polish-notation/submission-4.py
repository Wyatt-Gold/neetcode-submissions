class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(1, len(tokens) + 1):
            stack.append(tokens[i * -1])
        
        prev_nums = []
        signs = ('+', '-', '*', '/')
        while len(stack) > 1:
            temp = stack.pop()
            while temp not in signs:
                prev_nums.append(int(temp))
                temp = stack.pop()
            
            y, x = prev_nums.pop(), prev_nums.pop()
            if temp == '+':
                stack.append(x + y)
                print(x + y)
            elif temp == '*':
                stack.append(x * y)
                print(x * y)
            elif temp == '-':
                stack.append(x - y)
                print(x - y)
            else:
                stack.append(int(x / y))
                print(int(x / y))
        
        return int(stack.pop())
