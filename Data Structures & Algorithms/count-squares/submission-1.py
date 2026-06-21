class CountSquares:
    def __init__(self):
        self.ptFreq = defaultdict(int)
        self.pt = []

    def add(self, point: List(int)) -> None:
        self.ptFreq[tuple(point)] += 1
        self.pt.append(point)

    def count(self, point: List(int)) -> List(int):
        res = 0
        px, py = point
        for x, y in self.pt:
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += self.ptFreq[(x, py)] * self.ptFreq[(px, y)]
        return res
