class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            current = root
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = TrieNode()
                current = current.children[letter]
            current.is_end = True
            current.word = word

        visited = set()
        result = set()

        def dfs(row,col,node):
            if row <0 or col <0 or row>=len(board) or col >= len(board[0]):
                return
            if (row,col) in visited:
                return
            letter = board[row][col]
            if letter not in node.children:
                return
            node = node.children[letter]
            if node.is_end:
                result.add(node.word)
            
            visited.add((row,col))

            found = dfs(row+1,col,node) or dfs(row,col+1,node) or dfs(row-1,col,node) or dfs(row,col-1,node)

            visited.remove((row,col))
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row,col,root)
        return list(result)