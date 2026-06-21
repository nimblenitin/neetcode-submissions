class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        n1 = len(s1)
        n2 = len(s2)
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            poss1 = ord(s1[i]) - ord('a')
            poss2 = ord(s2[i]) - ord('a')
            s1Count[poss1] += 1
            s2Count[poss2] += 1
        if s1Count == s2Count:
            return True
        
        for j in range(n1, n2):
            poss2 = ord(s2[j]) - ord('a')
            s2Count[poss2] += 1
            s2Count[ord(s2[j - n1]) - ord('a')] -= 1
            if s1Count == s2Count:
                return True
        return False





            
            

