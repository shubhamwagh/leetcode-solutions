class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for i, val in enumerate(nums):
            if val !=0:
                nums[ind] = nums[i]
                ind = ind + 1
        
        for j in range(ind, len(nums)):
            nums[j] = 0
        
