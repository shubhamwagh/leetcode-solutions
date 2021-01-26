class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        x = [[i, nums.index(target - j)] for i, j in enumerate(nums) if nums.count(target - j) > 0 and nums.index(target-j)!=i]
        return x.pop()
    
        