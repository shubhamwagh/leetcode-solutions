class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
    
		if len(nums) == 1:
			return [nums]

		outList = [[nums[0]]]        
		perms = 1

		for n in nums[1:]:

			perms += 1
			tempOutList = []                        

			for lst in outList:
				for i in range(perms):
					tempOutList.append(lst[:i] + [n] + lst[i:])

			outList = tempOutList

		return outList