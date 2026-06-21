class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxW = 0
        while l < r:
            curW = (r - l) * min(heights[l], heights[r])
            maxW = max(maxW, curW)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxW
