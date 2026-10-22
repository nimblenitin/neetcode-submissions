class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tC, sC = {}, {}
        
        for c in t:
            tC[c] = tC.get(c, 0) + 1
        have, need = 0, len(tC)
        l, r = 0, 0
        res, resL = float("inf"), (0, 0)
        for ch in s:
            sC[ch] = sC.get(ch, 0) + 1

            if ch in tC and tC[ch] == sC[ch]:
                have += 1
            
            while have == need:
                if res > (r - l + 1):
                    res = (r - l + 1)
                    resL = (l, r)
                
                sC[s[l]] -= 1
                if s[l] in tC and sC[s[l]] < tC[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = resL
        return s[l: r + 1] if res != float("inf") else ""
 