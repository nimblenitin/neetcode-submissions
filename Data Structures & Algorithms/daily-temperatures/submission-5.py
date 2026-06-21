class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                prevI, prevV = stack.pop()
                output[prevI] = i - prevI
            stack.append((i, v))
        return output