class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        perms = [[]]
        for n in nums:
            tempPerm = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    tempPerm.append(pCopy)
            perms = tempPerm
        return perms

