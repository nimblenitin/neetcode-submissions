class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        res = set()
        visit = set()
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [-1, 0], [0 , 1], [0, -1]]
        def dfs(r, c, word, node):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] not in node.children or
                (r, c) in visit):
                return

            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.word:
                res.add(word)
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc, word, node)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)