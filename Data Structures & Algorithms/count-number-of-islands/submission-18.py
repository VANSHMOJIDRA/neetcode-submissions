class Solution:
    def numIslands(self,grid:list[list[str]])-> int:
        def dfs(row,col):
            if row < 0 or col< 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                        dfs(row,col)
                        count += 1
        return count