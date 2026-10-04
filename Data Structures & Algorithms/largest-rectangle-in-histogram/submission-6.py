class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []

        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                pI, pV = stack.pop()
                maxA = max(maxA, pV * (i - pI))
                start = pI
            stack.append([start, v])
        
        while stack:
            pI, pV = stack.pop()
            maxA = max(maxA, pV * (len(heights) - pI))
        return maxA

