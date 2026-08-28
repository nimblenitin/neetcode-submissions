class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nS1, nS2 = set(nums1), set(nums2)
        n1r, n2r = [], []
        for n1 in nS1:
            if n1 not in nS2:
                n1r.append(n1)

        for n2 in nS2:
            if n2 not in nS1:
                n2r.append(n2)
        
        return [n1r, n2r]
