class CountSquares:
    def __init__(self):
        self.pts = []
        self.ptsFreq = defaultdict(int)

    def add(self, point: List(int)) -> None:
        self.pts.append(point)
        self.ptsFreq[tuple(point)] += 1
    
    def count(self, point: List(int)) -> List(int):
        res = 0
        px, py = point
        for x, y in self.pts:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            res += self.ptsFreq[(x, py)] * self.ptsFreq[(px, y)]
        return res

