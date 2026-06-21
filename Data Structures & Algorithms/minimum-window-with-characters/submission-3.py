class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount, window = {}, {}

        if len(t) > len(s):
            return ""
        
        for v in t:
            tCount[v] = tCount.get(v, 0) + 1
        
        res, resLen = (-1, -1), float("inf")
        l = 0
        have, need = 0, len(tCount)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tCount and tCount[s[r]] == window[s[r]]:
                have += 1
                while have == need:
                    if resLen > (r - l + 1):
                        resLen = (r - l + 1)
                        res = (l, r)
                    window[s[l]] -= 1
                    if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""



                