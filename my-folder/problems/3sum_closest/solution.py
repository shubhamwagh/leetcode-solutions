class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        length = len(nums)
        result = nums[0] + nums[1] + nums[length-1]
        for ind in range(0, length - 2):
            if ind >0 and nums[ind] == nums[ind-1]:
                continue
            low = ind + 1
            high = length - 1
            
            while (low < high):
                total = nums[ind] + nums[low] + nums[high]
                if total < target:
                    low+=1
                elif total > target:
                    high-=1
                else:
                    low+=1
                    high-=1
                    while low < high and nums[low] == nums[low+1]:
                        low+=1
                    while low < high and nums[high] == nums[high-1]:
                        high-=1 
                if abs(total - target) < abs(result - target):
                    result = total
        return result  
        