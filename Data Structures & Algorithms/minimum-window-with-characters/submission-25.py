class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        sC, tC = {}, {}
        l = 0
        for c in t:
            tC[c] = tC.get(c, 0) + 1
        have, need = 0, len(tC)
        resLen, res = float("inf"), [0, 0]
        for r in range(len(s)):
            ch = s[r]
            sC[ch] = sC.get(ch, 0) + 1

            if ch in tC and sC[ch] == tC[ch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]

                sC[s[l]] -= 1 
                if s[l] in tC and sC[s[l]] < tC[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""
