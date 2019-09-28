class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

                
                
        x = [[i, nums.index(target-j)] for i,j in enumerate(nums) if nums.count(target-j) > 0 and nums.index(target-j)!=i]
         
        return x.pop()   