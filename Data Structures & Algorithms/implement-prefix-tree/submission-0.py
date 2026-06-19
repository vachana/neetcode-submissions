class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.isend = True


    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]
        
        return node.isend
            
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]
        
        return True

    # For All,
    # TC: O(m) when m is word lenght
    # SC: O(total characters across all words), but shared prefixes reduce it significantly vs. a hash set.
    # It means: in the worst case, you create one node per character across all words — which happens when no prefixes are shared at all.
        