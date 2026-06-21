class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for s in strs:
            ordList = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                ordList[idx] += 1
            anagramDict[tuple(ordList)].append(s)
        return list(anagramDict.values())
