class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        num_island = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":   
                    self.search_neighbour_cells(grid, i, j)
                    num_island +=1
        return num_island
    
    def search_neighbour_cells(self, grid, i, j):
        if i < 0 or i >= len(grid) or j< 0 or j>=len(grid[0]) or grid[i][j]!="1":
            return
        grid[i][j] = "0"
        self.search_neighbour_cells(grid, i, j+1)
        self.search_neighbour_cells(grid, i, j-1)
        self.search_neighbour_cells(grid, i+1, j)
        self.search_neighbour_cells(grid, i-1, j)
        