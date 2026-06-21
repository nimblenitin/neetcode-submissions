class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount, window = {}, {}

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        l = 0
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(tCount)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tCount and tCount[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in tCount and tCount[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

                