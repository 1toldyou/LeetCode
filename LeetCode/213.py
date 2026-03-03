class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        dp1 = [0] * n
        dp2 = [0] * n

        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])

        dp2[0] = 0
        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

        return max(dp1[-2], dp2[-1])