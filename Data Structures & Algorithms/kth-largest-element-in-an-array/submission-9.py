class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            left = mid = l
            right = r
            pivot = nums[r]

            while mid <= right:
                if nums[mid] < pivot:
                    nums[left], nums[mid] = nums[mid], nums[left]
                    mid += 1
                    left += 1
                elif nums[mid] > pivot:
                    nums[right], nums[mid] = nums[mid], nums[right]
                    right -= 1
                else:
                    mid += 1
                
            if k < left:
                return quickselect(l, left - 1)
            elif k > right:
                return quickselect(right + 1, r)
            else:
                return nums[k]

        return quickselect(0, len(nums) - 1)

