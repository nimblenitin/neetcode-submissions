class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        idxDict = {v: i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                val = stack.pop()
                curIdx = idxDict[val]
                res[curIdx] = nums2[i]
            
            if nums2[i] in idxDict:
                stack.append(nums2[i])
        return res
