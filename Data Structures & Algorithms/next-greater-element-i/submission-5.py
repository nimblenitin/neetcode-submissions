class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1In = {}
        res = [-1] * len(nums1)
        for i, v in enumerate(nums1):
            nums1In[v] = i
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                valIdx = nums1In[val]
                res[valIdx] = nums2[i]
            if nums2[i] in nums1In:
                stack.append(nums2[i])
        return res

