class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26 
        n1, n2 = len(s1), len(s2)
        for i in range(n1):
            os1 = ord(s1[i]) - ord('a')
            os2 = ord(s2[i]) - ord('a')
            s1Count[os1] += 1
            s2Count[os2] += 1
        if s1Count == s2Count:
            return True
        
        for j in range(n1, n2):
            nos2 = ord(s2[j]) - ord('a')
            s2Count[nos2] += 1
            pastidx = j - n1
            pastord = ord(s2[pastidx]) - ord('a')
            s2Count[pastord] -= 1
            if s1Count == s2Count:
                return True
        return False


        


            