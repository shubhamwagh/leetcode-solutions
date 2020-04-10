class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = float("inf")
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min_val:
            self.min_val = x        

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_val:
            self.update_min_val()
        
    def update_min_val(self):
        new_min = float("inf")
        for val in self.stack:
            if val < new_min:
                new_min = val
        self.min_val = new_min        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()