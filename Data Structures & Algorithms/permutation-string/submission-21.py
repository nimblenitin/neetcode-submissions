class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1C = [0] * 26
        s2C = [0] * 26

        for i in range(len(s1)):
            s1C[ord(s1[i]) - ord('a')] += 1
            s2C[ord(s2[i]) - ord('a')] += 1
        if s1C == s2C:
            return True
        
        for i in range(len(s1), len(s2)):
            s2C[ord(s2[i]) - ord('a')] += 1
            lC = s2[i - len(s1)]
            lO = ord(lC) - ord('a')
            s2C[lO] -= 1
            if s1C == s2C:
                return True
        return False