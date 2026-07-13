class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curH = (r - l) * min(heights[l], heights[r])
            maxA = max(curH, maxA)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA
