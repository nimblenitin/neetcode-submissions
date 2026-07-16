class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                t, sI = stack.pop()
                output[sI] = i - sI
            stack.append([v, i])
        return output