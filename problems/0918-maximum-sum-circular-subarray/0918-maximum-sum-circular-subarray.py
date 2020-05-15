class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        K = self.max_sub_array(A)
        cs = sum(A)
        K_new = self.max_sub_array([i * -1 for i in A])
        cs += K_new
        
        if cs > K and cs!=0:
            return cs
        else:
            return K
        
        
        
    def max_sub_array(self, nums: List[int]) -> int:
        #Kadane's algorithm
        max_current = max_global = nums[0]
        
        for ind in range(1, len(nums)):
            max_current = max(nums[ind], max_current + nums[ind])
            if max_current > max_global:
                max_global = max_current
        
        return max_global