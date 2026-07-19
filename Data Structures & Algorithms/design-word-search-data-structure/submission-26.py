class TrieNode():   
    def __init__(self):
        self.child = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = TrieNode()
            cur = cur.child[ch]
        cur.word = True

    def search(self, word: str) -> bool:
        
        def dfs(j, node):
            for j in range(j, len(word)):
                c = word[j]
                if c == ".":
                    for ch in node.child.keys():
                        if dfs(j + 1, node.child[ch]):
                            return True
                    return False
                else:
                    if c not in node.child:
                        return False
                    node = node.child[c]
            return node.word
        return dfs(0, self.root)


                        


