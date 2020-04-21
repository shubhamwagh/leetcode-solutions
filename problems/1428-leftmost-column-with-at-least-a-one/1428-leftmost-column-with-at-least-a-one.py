# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        row, col = binaryMatrix.dimensions()
        
        current_row = 0
        current_col = col -1
        
        while current_row < row and current_col >=0:
            
            if binaryMatrix.get(current_row, current_col) ==0:
                current_row +=1
            else:
                current_col -=1
            
        if current_col == col -1:
            return -1
        else:
            return current_col + 1