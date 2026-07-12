class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        n1, n2 = len(s1), len(s2)
        for i in range(n1):
            s1o = ord(s1[i]) - ord('a')
            s2o = ord(s2[i]) - ord('a')

            s1Count[s1o] += 1
            s2Count[s2o] += 1
        if s1Count == s2Count:
            return True
        
        for j in range(n1, n2):
            s2Count[ord(s2[j]) - ord('a')] += 1
            ch = s2[j - n1]
            pastchord = ord(ch) - ord('a')
            s2Count[pastchord] -= 1
            if s1Count == s2Count:
                return True
        return False
        

