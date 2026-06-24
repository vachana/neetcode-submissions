class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []
        
        for c in tokens:
            if stack and c in operands:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(b - a)
                    # tokens=["1","2","+","3","*","4","-"]->((2+1)*3)-4, 4 should be a, else it will be 4-9 instead of 9-4
                elif c == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
             # a//b trucates towards -infinty (-7//2 = -4 not -3(towards 0))
            else: 
                stack.append(int(c))
        return (stack[-1])

        # O(n) for both
