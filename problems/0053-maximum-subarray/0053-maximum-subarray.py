class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algorithm
        max_current = max_global = nums[0]
        
        for ind in range(1, len(nums)):
            max_current = max(nums[ind], max_current + nums[ind])
            if max_current > max_global:
                max_global = max_current
        
        return max_global