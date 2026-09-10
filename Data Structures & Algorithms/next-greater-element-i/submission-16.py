class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums1i = {v: i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)
        for r in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[r]:
                curI = stack.pop()
                if nums2[curI] in nums1i:
                    res[nums1i[nums2[curI]]] = nums2[r]
            stack.append(r)
        return res


        