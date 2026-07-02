class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1 = nums1
        num2 = nums2

        total = len(nums1) + len(nums2)
        half = total // 2
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        l = 0
        r = len(num1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            Aleft = num1[i] if i >= 0 else float("-inf")
            Bleft = num2[j] if j >= 0 else float("-inf")
            Aright = num1[i + 1] if (i + 1) < len(num1) else float("inf")
            Bright = num2[j + 1] if (j + 1) < len(num2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

                
