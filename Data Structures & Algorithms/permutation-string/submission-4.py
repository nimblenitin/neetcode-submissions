class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        n1 = len(s1)
        n2 = len(s2)
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        if s1_count == s2_count:
            return True
        for i in range(n1, n2):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - n1]) - ord('a')] -= 1
            if s1_count == s2_count:
                return True
        return False

            
            

