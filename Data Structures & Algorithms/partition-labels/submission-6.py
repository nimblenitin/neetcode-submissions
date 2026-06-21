class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}

        for i, v in enumerate(s):
            lastIdx[v] = i
        
        res = []
        end = lastIdx[s[0]]
        curLen = 0
        for i, v in enumerate(s):
            curLen += 1
            end = max(end, lastIdx[v])
            if end == i:
                res.append(curLen)
                curLen = 0
        return res