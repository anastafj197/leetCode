# Python Solution for leetCode problem 200 
# Letter Combinations of a Phone Number

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        num_islands = 0
        
        # Iterate through all spaces in the grid 
        # Once we find land (1) call dfs to check neighbors 
        # After the dfs completes incriment num_islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    num_islands += 1
                    
        return num_islands

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
