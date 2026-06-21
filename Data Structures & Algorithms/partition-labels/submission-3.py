class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex= {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        count = 0
        end = 0
        res = []
        for i, c in enumerate(s):
            count += 1
            end = max(lastIndex[c], end)
            if i == end:
                res.append(count)
                count = 0
        return res