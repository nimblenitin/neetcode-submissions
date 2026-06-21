class CountSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        totSq = 0
        for x, y in self.pts:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            
            totSq += self.freq[(px, y)] * self.freq[(x, py)]
        return totSq
            

 