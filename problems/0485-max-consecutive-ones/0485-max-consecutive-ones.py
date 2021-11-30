class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_ones = 0
        max_count_ones = 0
        for item in nums:
            if item:
                count_ones += 1
                if count_ones > max_count_ones:
                    max_count_ones = count_ones
            else:
                count_ones = 0
                
        return max_count_ones