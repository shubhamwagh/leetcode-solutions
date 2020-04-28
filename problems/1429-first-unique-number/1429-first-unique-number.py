class FirstUnique:

    def __init__(self, nums: List[int]):
        self.deque = collections.deque()
        self.map = {}
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        
        if len(self.deque) ==0:
            return -1
        
        while len(self.deque) > 0 and self.deque[0] in self.map and self.map[self.deque[0]] >=2:
            self.deque.popleft()
        
        if len(self.deque) ==0:
            return -1

        return self.deque[0]
         

    def add(self, value: int) -> None:
        
        if value in self.map:
            self.map[value] +=1
        else:
            self.map[value] = 1
        
        self.deque.append(value)
        
            
            
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)