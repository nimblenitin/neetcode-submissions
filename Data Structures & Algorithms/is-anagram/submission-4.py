class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        an_list = [0]* 26
        for i in range(len(s)):
            an_list[ord(s[i]) - ord('a')] += 1
            an_list[ord(t[i]) - ord('a')] -= 1
        for val in an_list:
            if val != 0:
                return False
        return True
            
