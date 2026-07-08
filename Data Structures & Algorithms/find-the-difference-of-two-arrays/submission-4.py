class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1S, nums2S = set(nums1), set(nums2)
        res1, res2 = [], []
        for n1 in nums1S:
            if n1 not in nums2S:
                res1.append(n1)
        
        for n2 in nums2S:
            if n2 not in nums1S:
                res2.append(n2)
            
        return [res1, res2]
