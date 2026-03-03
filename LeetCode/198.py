class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            if i <= 1:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i], dp[i-3]+nums[i])
        # print(dp)
        return max(dp)