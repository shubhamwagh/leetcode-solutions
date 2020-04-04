class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:     
        result = []
        nums.sort()
        length = len(nums)
        
        for ind in range(0, length-3):
            if ind != 0 and nums[ind] == nums[ind -1]:
                continue
            for ind_r in range(ind+1, length-2):
                if ind_r != ind+1 and nums[ind_r] == nums[ind_r - 1]:
                    continue
                low = ind_r + 1
                high = length - 1
                
                while(low < high):
                    a = nums[ind]
                    b = nums[ind_r]
                    c = nums[low]
                    d = nums[high]
                    total = a +b + c+d
                    
                    if total < target:
                        low+=1
                    elif total > target:
                        high-=1
                    else:
                        result.append([a,b,c, d])
                        while low < high and nums[low] == nums[low+1]:
                            low+=1
                        while low < high and nums[high] == nums[high-1]:
                            high-=1
                        low+=1
                        high-=1                    
                    
        return result    

        
    
                        
        