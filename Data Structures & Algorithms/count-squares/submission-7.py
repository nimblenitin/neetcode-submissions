class CountSquares:

    def __init__(self):
        self.freq =  defaultdict(int)
        self.pt = []

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1
        self.pt.append(point)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for px, py in self.pt:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            
            res += self.freq[(x, py)] * self.freq[(px, y)]
        return res 
