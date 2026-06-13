class Solution:
    def pacificAtlantic(self,heights:list[list[int]]) -> list[list[int]]:
        atlantic = set()
        pacific = set()

        def dfs(row,col,visited,prevh):
            if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]):
                return
            if (row,col) in visited:
                return
            if heights[row][col] < prevh:
                return
            visited.add((row,col))
            dfs(row+1,col,visited,heights[row][col])
            dfs(row,col+1,visited,heights[row][col])
            dfs(row-1,col,visited,heights[row][col])
            dfs(row,col-1,visited,heights[row][col])
        for row in range(len(heights)):
            dfs(row,0,pacific,heights[row][0])
        for col in range(len(heights[0])):
            dfs(0, col,pacific,heights[0][col])
        for row in range(len(heights)):
            dfs(row,len(heights[0])-1 , atlantic,heights[row][len(heights[0]) -1])
        for col in range(len(heights[0])):
            dfs(len(heights) -1 , col, atlantic , heights[len(heights) -1][col])
        return list(pacific & atlantic)