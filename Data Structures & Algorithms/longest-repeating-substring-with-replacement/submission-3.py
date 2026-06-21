class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curC = {}
        l = 0
        maxF = 0
        maxL = 0
        for r in range(len(s)):
            curC[s[r]] = curC.get(s[r], 0) + 1
            maxF = max(maxF, curC[s[r]])
            while (r - l + 1) - maxF > k:
                curC[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
        return maxL
