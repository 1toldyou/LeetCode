class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            for j in range(i-1, i-3, -1):
                dp[i] += dp[j]

        return dp[-1]