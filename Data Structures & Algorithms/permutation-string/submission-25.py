class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1L = [0] * 26
        s2L = [0] * 26

        for i in range(len(s1)):
            s1C = s1[i]
            s2C = s2[i]
            s1L[ord(s1C) - ord('a')] += 1
            s2L[ord(s2C) - ord('a')] += 1

        if s1L == s2L:
            return True
        
        for j in range(len(s1), len(s2)):
            s2C = s2[j]
            s2L[ord(s2C) - ord('a')] += 1
            l = j - len(s1)
            ch = s2[l]
            s2L[ord(ch) - ord('a')] -= 1
            if s1L == s2L:
                return True
        return False