class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        visited = set()
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if self._explore_island(grid, row, col, visited):
                    count += 1
        return count
        
    def _explore_island(self, grid, row, col, visited):
        row_in_bounds = 0 <= row < len(grid)
        col_in_bounds = 0 <= col < len(grid[0])
        
        if not row_in_bounds or not col_in_bounds:
            return False
        
        if grid[row][col] == '0':
            return False
        
        key = str(row) + ',' + str(col)
        if key in visited:
            return False
        
        visited.add(key)
        
        neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        
        for r, c in neighbours:
            self._explore_island(grid, r, c, visited)
        
        return True