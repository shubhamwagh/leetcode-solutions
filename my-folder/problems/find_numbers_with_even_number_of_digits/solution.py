class Solution:
    
    def get_digit_count(self, num: int):
        return len(str(num))
    
    def findNumbers(self, nums: List[int]) -> int:
        
        even_count = 0
        for item in nums:
            if self.get_digit_count(item) % 2 ==0:
                even_count += 1
            else:
                continue
        return even_count        
        