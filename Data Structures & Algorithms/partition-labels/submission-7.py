class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}

        for i, c in enumerate(s):
            lastIdx[c] = i
        
        res = []
        curEnd = curLen = 0
        for i in range(len(s)):
            curLen += 1
            curEnd = max(curEnd, lastIdx[s[i]])
            if i == curEnd:
                res.append(curLen)
                curLen = 0
        return res
