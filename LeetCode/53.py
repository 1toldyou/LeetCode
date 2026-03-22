class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)

        accu = 0
        for num in nums:
            if accu < 0:c
                accu = 0
            accu += num
            ans = max(ans, accu)

        return ans