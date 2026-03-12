class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        print(intervals)

        dp = [1] * n

        for i in range(1, n):
            bestPrev = 0
            for j in range(i-1, -1, -1):
                if intervals[j][1] <= intervals[i][0]:
                    # print(f"{intervals[i]} can go after {intervals[j]}")
                    bestPrev = max(bestPrev, dp[j])
            dp[i] += bestPrev
        print(dp)
        return n - max(dp)
