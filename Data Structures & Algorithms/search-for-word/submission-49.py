class Solution:
    def exist(self,board:list[list[str]],word:str) -> bool:
        visited = set()
        def solve(row,col,i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if board[row][col] != word[i]:
                return False
            if (row,col) in visited:
                return False
            if row > len(word):
                return False
            
            visited.add((row,col))

            found = solve(row+1,col,i+1) or solve(row,col+1,i+1) or solve(row-1,col,i+1) or solve(row,col-1,i+1)
        
            visited.remove((row,col))

            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if solve(row,col,0):
                    return True
        return False 