class Solution:
    
    def sqsum(self, n):
        result = 0
        
        while (n > 0):
            r = n % 10
            result += r **2
            n = n //10
        return result   
    
    def isHappy(self, n: int) -> bool:
        
        past = set()
        
        while self.sqsum(n) not in past:
            res = self.sqsum(n)
            print(res)
            if res == 1:
                return True
            else:
                past.add(res)   
                n = res
        return False        