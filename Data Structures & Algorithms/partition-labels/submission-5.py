class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idxMap = {}
        for i, v in enumerate(s):
            idxMap[v] = i
        
        res = []
        end, len = 0, 0
        for i, v in enumerate(s):
            len += 1
            end = max(end, idxMap[v])
            if i == end:
                res.append(len)
                len = 0
        return res