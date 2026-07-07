class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set, nums2set = set(nums1), set(nums2)
        res1, res2 = [], []

        for n in nums1set:
            if n not in nums2set:
                res1.append(n)

        for n in nums2set:
            if n not in nums1set:
                res2.append(n)
        
        return [res1, res2]