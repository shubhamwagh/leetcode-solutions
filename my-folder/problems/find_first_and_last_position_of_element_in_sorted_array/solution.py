class Solution:
    def find_left_most(self, nums, target):
        left, right = 0, len(nums) - 1
        left_most = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                left_most = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left_most
    

    def find_right_most(self, nums, target):
        left, right = 0, len(nums) - 1
        right_most = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                right_most = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid - 1
        return right_most

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.find_left_most(nums, target), self.find_right_most(nums, target)]
        