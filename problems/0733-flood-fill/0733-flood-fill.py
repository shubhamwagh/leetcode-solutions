class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        self.search_neighbour_cells(image, sr, sc, oldColor, newColor)
        return image
        
        
    
#     def search_neighbour_cells(self, image, i, j, oldColor, newColor):
#         if i < 0 or i >= len(image) or j< 0 or j>=len(image[0]) or image[i][j]!=oldColor:
#             return
#         image[i][j] = newColor
#         self.search_neighbour_cells(image, i, j+1, oldColor, newColor)
#         self.search_neighbour_cells(image, i, j-1, oldColor, newColor)
#         self.search_neighbour_cells(image, i+1, j, oldColor, newColor)
#         self.search_neighbour_cells(image, i-1, j, oldColor, newColor)
    
    def search_neighbour_cells(self, image, i, j, oldColor, newColor):
        if image[i][j] == oldColor:
            image[i][j] = newColor
            if j+1 < len(image[0]): self.search_neighbour_cells(image, i, j+1, oldColor, newColor)
            if j >= 1: self.search_neighbour_cells(image, i, j-1, oldColor, newColor)
            if i+1 < len(image): self.search_neighbour_cells(image, i+1, j, oldColor, newColor)
            if i >=1: self.search_neighbour_cells(image, i-1, j, oldColor, newColor)