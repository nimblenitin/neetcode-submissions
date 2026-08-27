class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1S, nums2S = set(nums1), set(nums2)

        n1, n2 = [], []

        for num1 in nums1S:
            if num1 not in nums2S:
                n1.append(num1)

        for num2 in nums2S:
            if num2 not in nums1S:
                n2.append(num2)
        
        return [n1, n2]