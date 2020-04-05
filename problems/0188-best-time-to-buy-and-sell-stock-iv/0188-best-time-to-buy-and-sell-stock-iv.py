class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        max_transactions = k
        if prices == None or len(prices)==0:
            return 0
        if (max_transactions >=  len(prices)/2):
            maxPro = 0
            for i in range(0, len(prices)-1):
                if prices[i+1] > prices[i]:
                    maxPro += prices[i+1] - prices[i]
            return maxPro
       
#         profit = [[0 for d in range(0, len(prices))] for k in range(0, max_transactions + 1)]        
#         for k in range(1, max_transactions + 1):
#             max_so_far = float("-inf")
#             for d in range(1, len(prices)):
#                 previous_day_profit = profit[k][d-1]
#                 # profit_for_different_selling_options = [0] * d
#                 # for i in range(0, d):
#                 #     profit_for_different_selling_options[i] = - prices[i] + profit[k-1, i]
#                 # profit_from_selling_current = prices[d] + max(profit_for_different_selling_options) 
#                 max_so_far = max(max_so_far, profit[k-1][d-1] - prices[d-1])
#                 profit[k][d] = max(previous_day_profit, prices[d] + max_so_far)
                
                
#         return profit[-1][-1]

        
        profit = [[0 for d in range(0, len(prices))] for k in range(0, 2)]
        print(profit)
        for k in range(1, max_transactions+1):
            max_so_far = profit[0][0] - prices[0]
            for d in range(1, len(prices)):
                previous_day_profit = profit[1][d-1]
                profit[1][d] = max(previous_day_profit, prices[d] + max_so_far)
                max_so_far = max(max_so_far, profit[0][d] - prices[d])
                profit[0][d] = profit[1][d]
        return profit[0][-1]