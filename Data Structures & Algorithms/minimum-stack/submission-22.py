class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minS.append(self.minS[-1] if self.minS and self.minS[-1] < val else val)

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minS[-1]
