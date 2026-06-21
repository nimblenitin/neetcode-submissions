class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                j, _ = stack.pop()
                output[j] = i - j
            stack.append((i, v))
        return output