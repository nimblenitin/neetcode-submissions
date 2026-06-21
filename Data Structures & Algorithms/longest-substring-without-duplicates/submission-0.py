class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        uChar = set()
        for r in range(len(s)):
            while s[r] in uChar:
                uChar.remove(s[l])
                l += 1
            uChar.add(s[r])
            res = max(res, r - l + 1)
        return res