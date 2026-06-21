class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            dp.append(nums[0])

            for i in range(1, len(nums)):
                if nums[i] > dp[-1]:
                    dp.append(nums[i])
                    continue
                idx = bisect_left(dp, nums[i])
                dp[idx] = nums[i]
            return len(dp)
        return lis([e[1] for e in envelopes])