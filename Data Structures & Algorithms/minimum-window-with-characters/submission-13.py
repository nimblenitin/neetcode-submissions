class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        sC, tC = {}, {}

        for c in t:
            tC[c] = tC.get(c, 0) + 1
        
        have, need = 0, len(tC)
        resLen, res = float("inf"), (-1, -1)
        l = 0
        for r in range(len(s)):
            c = s[r]
            sC[s[r]] = sC.get(s[r], 0) + 1

            if c in tC and sC[c] == tC[c]:
                have += 1
            
            while have == need:
                if resLen > (r - l + 1):
                    resLen = (r - l + 1)
                    res = (l, r)
                
                sC[s[l]] -= 1
                if s[l] in tC and sC[s[l]] < tC[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""
 

