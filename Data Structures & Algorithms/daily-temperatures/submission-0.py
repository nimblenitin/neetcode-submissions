class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp, i
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                mint, minti = stack.pop()
                res[minti] = (i - minti)
            stack.append([v, i])
        return res