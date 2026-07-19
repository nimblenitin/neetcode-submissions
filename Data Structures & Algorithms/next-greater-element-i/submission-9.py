class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1I = {}
        res = [-1] * len(nums1)
        stack = []

        for i, v in enumerate(nums1):
            nums1I[v] = i

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                res[nums1I[val]] = nums2[i]
            
            if nums2[i] in nums1I:
                stack.append(nums2[i])
        return res