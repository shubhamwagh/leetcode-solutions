class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def is_single_element(idx):
            if idx == len(nums) - 1:
                return True
            elif idx % 2 == 0:
                return nums[idx] != nums[idx + 1]
            else:
                return nums[idx] != nums[idx - 1]
        

        left, right = 0, len(nums) - 1
        single_element_index = -1

        while left <= right:
            mid = (left + right) // 2

            if is_single_element(mid):
                single_element_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[single_element_index]


        