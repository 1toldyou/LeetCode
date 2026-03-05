class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        dp = [0] * n
        dp[1] = max(0, prices[1]-prices[0])

        for i in range(2, n):
            for j in range(i-1, -1, -1):
                dp[i] = max(dp[i], dp[j], prices[i]-prices[j]+(dp[j-2] if j-2 >= 0 else 0))  # # do nothing vs. sell whatever brought from another day

        return max(dp)
        