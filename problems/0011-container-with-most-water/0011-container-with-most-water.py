class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        pointer_one = 0
        pointer_two = len(height) - 1
        
        
        while pointer_one < pointer_two:
            w = pointer_two - pointer_one
            h = min(height[pointer_one], height[pointer_two])
            area = w * h
            max_area = max(area, max_area)
            
            if height[pointer_one] < height[pointer_two]:
                pointer_one += 1
            else:
                pointer_two -= 1
                
        return max_area