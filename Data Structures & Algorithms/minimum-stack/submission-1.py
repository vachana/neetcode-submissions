class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val,self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

# TC: O(1) and SC: O(n)
# O(2n) simplifies to O(n) — constants get dropped in Big O notation. We only care about how space scales with input size, and two stacks both growing linearly is still linear growth.
        
