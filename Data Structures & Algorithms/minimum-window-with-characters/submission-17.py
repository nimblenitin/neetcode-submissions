class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        sC, tC = {}, {}

        for c in t:
            tC[c] = tC.get(c, 0) + 1

        have, need = 0, len(tC)
        res, resLen = (-1, -1), float("inf")
        l = 0
        for r in range(len(s)):
            ch = s[r]
            sC[ch] = sC.get(ch, 0) + 1
            if ch in tC and sC[ch] == tC[ch]:
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
        return s[l:r + 1] if resLen != float("inf") else ""

            
            
             