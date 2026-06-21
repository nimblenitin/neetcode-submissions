class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            top, bottum = l, r
            for i in range(r - l):
                topLeft = matrix[top][l + i]
                
                matrix[top][l + i] = matrix[bottum - i][l]

                matrix[bottum- i][l] = matrix[bottum][r - i]

                matrix[bottum][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft
            l += 1
            r -= 1

                











