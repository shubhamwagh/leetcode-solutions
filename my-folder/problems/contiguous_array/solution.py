class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        map = {}
        subarr = count = 0
        
        for ind in range(0,len(nums)):
            
            if nums[ind] == 0:
                count-=1
            else:
                count+=1
            
            if count == 0:
                subarr = ind + 1
            
            if count in map:
                subarr = max(subarr, ind - map[count])
            else:
                map[count] = ind
        return subarr        
                
                
        
        

                
            
        
        