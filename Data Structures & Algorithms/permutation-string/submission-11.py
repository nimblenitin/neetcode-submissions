class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        n1 = len(s1)
        n2 = len(s2)

        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(n1):
            o1 = ord(s1[i]) - ord("a")
            o2 = ord(s2[i]) - ord("a")
            s1count[o1] += 1
            s2count[o2] += 1
        if s1count == s2count:
                return True
            
        for j in range(n1, n2):
            nord = ord(s2[j]) - ord("a")
            s2count[nord] += 1
            pos = ord(s2[j - n1]) - ord("a")
            s2count[pos] -= 1
            if s1count == s2count:
                return True
        return False        


        