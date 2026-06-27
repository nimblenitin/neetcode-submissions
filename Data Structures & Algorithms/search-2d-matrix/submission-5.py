class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS - 1

        while l <= r:
            m = (l + r) // 2 
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][COLS - 1]:
                l = m + 1
            else:
                break
        
        if not (l <= r):
            return False

        m = (l + r) // 2
        l = 0
        r = COLS - 1

        while l <= r:
            c = (l + r) // 2
            if target > matrix[m][c]:
                l = c + 1
            elif target < matrix[m][c]:
                r = c - 1
            else:
                return True
        return False