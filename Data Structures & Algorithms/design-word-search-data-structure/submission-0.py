class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            
        node.isEnd = True
        

    def search(self, word: str) -> bool:

        def dfs(node, index):
            if index == len(word):
                return node.isEnd
            
            ch = word[index]

            if ch == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], index+1)


        return dfs(self.root, 0)


# TC:
# addWord: O(m) — one node created/traversed per character, where m = word length.
# search (no wildcard): O(m) — straight path down the trie.
# search (with .): O(26^m) worst case — at each . you branch into all children, and if every character is . you explore every possible path.

# SC:
# addWord: O(m) per word — at most m new nodes created.
# search: O(m) — recursive call stack goes m levels deep (one level per character).
        
