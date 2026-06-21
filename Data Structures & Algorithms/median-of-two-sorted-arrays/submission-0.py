class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        m = n // 2
        if n % 2 == 1:
            return merged[m]
        else:
            return (merged[m-1] + merged[m]) / 2.0
            
