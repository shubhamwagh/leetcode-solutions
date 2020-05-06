class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
#         map = {}
#         for val in nums:
#             if val in map:
#                 map[val] +=1
#             else:
#                 map[val] = 1
                
#         max_val = 0
#         for key in map:
#             if map[key] > len(nums) // 2:
#                 max_val = key
#         return max_val
    
        nums.sort()
        return nums[len(nums) // 2]