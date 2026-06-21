class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tCount, sCount = {}, {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        res, resL = (-1, -1), float("inf")
        have, need = 0, len(tCount)
        l = 0
        for r in range(len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1
            while have == need:
                if resL > (r - l + 1):
                    resL = (r - l + 1)
                    res = (l, r)
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resL != float("inf") else ""
        
        


                