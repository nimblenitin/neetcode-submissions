class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.wordEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        root = TrieNode()
        for word in words:
            root.addWord(word)
        res = set() 
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                    (r, c) in visit or board[r][c] not in node.children):
                return 
            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.wordEnd:
                res.add(word)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, node, word)
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
