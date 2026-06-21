class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while left < right:
            top, bottum = left, right
            for i in range(right - left):
                topLeft = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottum - i][left]

                matrix[bottum - i][left] = matrix[bottum][right - i]

                matrix[bottum][right - i] = matrix[top + i][right]

                matrix[top + i][right] = topLeft
            left += 1
            right -= 1


                











