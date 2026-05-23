class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_end = True

        
    def search(self,word:str) -> bool:
        def solve(node,i):
            if i == len(word):
                return node.is_end
            letter = word[i]
            if letter == '.':
                for child in node.children.values():
                    if solve(child,i+1):
                        return True
            else:
                if letter not in node.children:
                    return False
                return solve(node.children[letter],i+1)
            return False
        return solve(self.root,0)