class Solution(object):
    '''
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==0:
            return 0
        if n ==1 or n==2:
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    '''    
        
    def tribonacci(self, n):
        
        a, b, c, = 0, 1, 1
        
        for i in range(n):
            a, b, c = b, c, a+b+c
            print(a, b, c)
        return a    
            