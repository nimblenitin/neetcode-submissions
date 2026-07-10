class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tCount, sCount = {}, {}

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        have, need = 0, len(tCount)
        res, resLen = (-1, -1), float("inf")
        l = 0
        for i, v in enumerate(s):
            sCount[v] = sCount.get(v, 0) + 1

            if v in tCount and sCount[v] == tCount[v]:
                have += 1
            while have == need:
                if resLen > (i - l + 1):
                    resLen = (i - l + 1)
                    res = (l, i)
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""


