class Solution:

    def permute(self, nums, arr=[], answers=[]):

        if len(nums) == 0 and arr not in answers:
            answers.append(arr.copy())

        for ind in range(0, len(nums)):
            array_without_current_number = [nums[i] for i in range(0, len(nums)) if ind != i]
            arr.append(nums[ind])
            self.permute(array_without_current_number, arr, answers)
            arr.pop()
        return answers

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.permute(nums, [], [])