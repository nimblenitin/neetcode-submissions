class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []

        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][0] > v:
                curV, curI = stack.pop()
                maxA = max(maxA, curV * (i - curI))
                start = curI
            stack.append((v, start))
        
        for val, idx in stack:
            maxA = max(maxA, val * (len(heights) - idx))
        return maxA
