class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottum = 0, len(matrix)

        while left < right and top < bottum:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottum):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottum):
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottum - 1][i])
            bottum -= 1

            for i in range(bottum - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
