class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums1I = {}

        for i, v in enumerate(nums1):
            nums1I[v] = i
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                res[nums1I[stack.pop()]] = nums2[i]

            if nums2[i] in nums1I:
                stack.append(nums2[i])
        return res