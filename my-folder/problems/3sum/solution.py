class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        length = len(nums)
        for ind in range(0, length - 2):
            if (ind > 0 and nums[ind]==nums[ind-1]):
                continue
            low = ind +1
            high = length - 1
            while(low < high):
                total = nums[ind] + nums[low] + nums[high]
                if total < 0:
                    low +=1
                elif total > 0 :
                    high-=1
                else:
                    result.append([nums[ind], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high -1]:
                           high-=1
                            
                    low+=1
                    high-=1
        return result                
                
        