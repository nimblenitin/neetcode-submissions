class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1M, s2M = {}, {}

        for i in range(len(s1)):
            s1M[s1[i]] = s1M.get(s1[i], 0) + 1
            s2M[s2[i]] = s2M.get(s2[i], 0) + 1

        if s1M == s2M:
            return True
        
        for j in range(len(s1), len(s2)):
            s2M[s2[j]] = s2M.get(s2[j], 0) + 1
            l = j - len(s1)
            s2M[s2[l]] -= 1
            if s2M[s2[l]] == 0:
                del s2M[s2[l]]
            if s1M == s2M:
                return True
        return False