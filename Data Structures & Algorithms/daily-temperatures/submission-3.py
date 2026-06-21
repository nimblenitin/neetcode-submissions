class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                curVal, curIdx = stack.pop()
                res[curIdx] = i - curIdx
            stack.append((v, i))
        return res