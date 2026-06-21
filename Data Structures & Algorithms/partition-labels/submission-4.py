class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI = {}
        for i, v in enumerate(s):
            lastI[v] = i
        count = 0
        end = 0
        res = []
        for i, v in enumerate(s):
            count += 1
            end = max(end, lastI[v])
            if i == end:
                res.append(count)
                count = 0
        return res

