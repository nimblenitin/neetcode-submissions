class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos = set()
        neg = set()
        res = []
        temp = [["."] * n for r in range(n)]
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in temp])
                return
            
            for c in range(n):
                if c in col or (r + c) in pos or (r - c) in neg:
                    continue
                
                temp[r][c] = "Q"
                col.add(c)
                pos.add(r + c)
                neg.add(r - c)
                backtrack(r + 1)

                temp[r][c] = "."
                col.remove(c)
                pos.remove(r + c)
                neg.remove(r - c)
        backtrack(0)
        return res



            
