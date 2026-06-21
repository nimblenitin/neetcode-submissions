class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        cFreqSet = {}
        l = 0
        res = 0
        for i in range(len(s)):
            cFreqSet[s[i]] = cFreqSet.get(s[i], 0) + 1
            if len(cFreqSet) <= 2:
                res = max(res, i - l + 1)
            while len(cFreqSet) > 2:
                cFreqSet[s[l]] -= 1
                if cFreqSet[s[l]] == 0:
                    cFreqSet.pop(s[l])
                l += 1
        return res
