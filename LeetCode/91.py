class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # viability check
        if s[0] == "0":
            return 0
        

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            one = int(s[i-1]) 
            two = int(s[i-2:i])
            # print(f"i={i} one={one} two={two}")
            if one != 0:
                dp[i] += dp[i-1]
            if two >= 10 and two <= 26:
                dp[i] += dp[i-2]

        return dp[n]       