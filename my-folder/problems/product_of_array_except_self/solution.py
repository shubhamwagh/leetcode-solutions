class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        
        
        for ind in range(1, len(nums)):
            result[ind] = result[ind -1] * nums[ind -1]
            
        right = 1
        for ind in range(len(nums)-1, -1, -1):
            result[ind] = right * result[ind]
            right = right * nums[ind]
        return(result)   