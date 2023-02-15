class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for ind in range(len(nums)):
            num_1 = nums[ind]
            num_2 = target - num_1
            if num_2 in hash_map:
                return [ind, hash_map[num_2]]
            hash_map[num_1] = ind
        return