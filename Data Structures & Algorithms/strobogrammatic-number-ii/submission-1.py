class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        reversiblePairs = [['0', '0'], ['1', '1'], ['8', '8'],
                            ['6', '9'], ['9', '6']]

        curStrLen = n % 2
        q = ["0", "1", "8"] if curStrLen == 1 else [""]

        while curStrLen < n:
            curStrLen += 2
            nextLevel = []

            for num in q:
                for pair in reversiblePairs:
                    if curStrLen != n or pair[0] != "0":
                        nextLevel.append(pair[0] + num + pair[1])
            q = nextLevel
        return q