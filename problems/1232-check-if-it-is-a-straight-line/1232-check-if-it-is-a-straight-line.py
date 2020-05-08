class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) == 2:
            return True
        
        
        first_point = coordinates[0]
        second_point = coordinates[1]
        
       
        for i in range(2, len(coordinates)):
            point = coordinates[i]
                        
            if (second_point[1] - first_point[1]) * (point[0] - first_point[0]) != (point[1] - first_point[1]) * (second_point[0] - first_point[0]) :
                return False
        return True