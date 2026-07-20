class TrieNode():
    def __init__(self):
        self.child = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        res = set()
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, word, node):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or board[r][c] not in node.child):
                return

            visit.add((r, c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, word, node)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)
