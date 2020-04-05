class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        if prices == None or len(prices) == 0:
            return 0
        for ind in range(0, len(prices) - 1):
            
            if prices[ind+1] > prices[ind]:
                profit+= prices[ind+1] - prices[ind]
        return profit        
            
                
            