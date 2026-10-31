class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for c in tokens:
            if not c in operators:
                stack.append(int(c))
                continue
            operand_b, operand_a = stack.pop(), stack.pop()
            if c == "+":
                stack.append(operand_a + operand_b)
            elif c == '-':
                stack.append(operand_a - operand_b)
            elif c == '*':
                stack.append(operand_a * operand_b)
            else:
                stack.append(int(operand_a / operand_b))
        
        return stack.pop()
        