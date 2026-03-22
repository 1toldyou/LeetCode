class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # viability check
        for i in range(n):
            if int(s[i]) == 0:
                if i == 0:
                    return 0
                elif int(s[i-1]) > 2:
                    return 0
        

        dp = [0] * n
        for i in range(n):
            num = int(s[i])
            if num == 0:
                dp[i] = 0
            elif num <= 2 and i < n-1 and int(s[i+1]) <= 6:
                dp[i] = 2
            else:
                dp[i] = 1

        print(dp)
        freqs = Counter(dp)
        twos = freqs.get(2, 0)
        zeros = freqs.get(0, 0)

        return 1 + max(0, (twos - zeros*2))

        