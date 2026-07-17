class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        op = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                lVal, lastI = stack.pop()
                op[lastI] = i - lastI
            stack.append([v, i])
        return op
