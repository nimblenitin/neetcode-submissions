class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        sC, tC = {}, {}

        for ch in t:
            tC[ch] = tC.get(ch, 0) + 1
        
        have, need = 0, len(tC)
        resLen, res = float("inf"), (-1, -1)

        l = 0
        for r in range(len(s)):
            curC = s[r]
            sC[curC] = sC.get(curC, 0) + 1
            if curC in tC and sC[curC] == tC[curC]:
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

