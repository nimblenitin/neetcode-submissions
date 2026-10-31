class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {v: i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            val = nums2[i]
            while stack and stack[-1] < val:
                v = stack.pop()
                idx = nums1Idx[v]
                res[idx] = val
            if val in nums1:
                stack.append(val)
        return res
        