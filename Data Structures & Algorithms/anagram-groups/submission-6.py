class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDic = defaultdict(list)

        for w in strs:
            oL = [0] * 26
            for s in w:
                cO = ord(s) - ord('a')
                oL[cO] += 1
            anaDic[tuple(oL)].append(w)
        return list(anaDic.values())

                

                
                