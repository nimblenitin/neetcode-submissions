class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or
                board[r][c] != word[i]):
                return False
            
            visit.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if dfs(nr, nc, i + 1):
                    return True
            visit.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False