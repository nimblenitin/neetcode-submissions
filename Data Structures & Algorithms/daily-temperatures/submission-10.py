class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        op = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                lastI, lastV = stack.pop()
                op[lastI] = i - lastI
            stack.append([i, v])
        return op