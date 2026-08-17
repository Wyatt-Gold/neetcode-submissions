class TreeNode:
    def __init__(self, c=None):
        self.c = c
        self.children = {}
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                curr_node.children[c] = TreeNode(c)
                curr_node = curr_node.children[c]
        if '' not in curr_node.children:
            curr_node.children[''] = None

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return False
        return '' in curr_node.children

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            else:
                return False
        return True
        