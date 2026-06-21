class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            cur_Area = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, cur_Area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea