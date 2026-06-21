class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversiblePairs = [["0", "0"], ["1", "1"], ["8", "8"], ["6", "9"], ["9", "6"]]

        curStrLen = n % 2
        q = ["1", "0", "8"] if n % 2 != 0 else [""]

        while curStrLen < n:
            level = []
            curStrLen += 2
            for num in q:
                for pair in reversiblePairs:
                    if curStrLen != n or pair[0] != "0":
                        level.append(pair[0] + num + pair[1])
            q = level
        return q