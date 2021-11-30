class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums, key=lambda x: abs(x))
        out = [x**2 for x in sorted_num]
        return out
        
        