class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        pairs.sort(reverse = True)
        for pos, speed in pairs:
            destTime = (target - pos) / speed
            stack.append(destTime)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

