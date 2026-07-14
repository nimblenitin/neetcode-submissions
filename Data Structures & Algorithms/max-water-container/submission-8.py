class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            curA = (r - l) * min(heights[l], heights[r])
            maxA = max(maxA, curA)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1  
        return maxA