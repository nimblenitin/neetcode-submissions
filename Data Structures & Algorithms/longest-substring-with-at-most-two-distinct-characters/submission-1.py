class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while len(freq) > 2:
                if s[l] in freq:
                    freq[s[l]] -= 1
                    
                    if freq[s[l]] == 0:
                        freq.pop(s[l])
                    l += 1
            res = max(res, r - l + 1)
        return res
            