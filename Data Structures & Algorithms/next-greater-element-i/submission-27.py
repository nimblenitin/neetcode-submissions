class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1H = {v: i for i, v in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)
        for n in nums2:
            while stack and stack[-1] < n:
                val = stack.pop()
                idx = nums1H[val]
                res[idx] = n
            else:
                if n in nums1H:
                    stack.append(n)
        return res