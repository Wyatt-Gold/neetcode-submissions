class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                curr_node.children[c] = TrieNode()
                curr_node = curr_node.children[c]
        curr_node.end_of_word = True 

    def search(self, word: str) -> bool:
        return self.helper(word, self.root)
    
    def helper(self, word, root) -> bool:
        curr_node = root
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for child in curr_node.children.values():
                    if self.helper(word[i+1:], child):
                        return True
                return False
            elif c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return False
        return curr_node.end_of_word
