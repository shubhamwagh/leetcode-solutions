class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
#         res = nums[0]
#         for val in nums[1:]:
#             res = res ^ val
#         return res
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            halves_are_even = (right - mid) % 2 ==0
            
            if nums[mid] == nums[mid + 1]:
                if halves_are_even:
                    left = mid + 2
                else:
                    right = mid -1
            elif nums[mid] == nums[mid - 1]:
                if halves_are_even:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]
        return nums[left]            