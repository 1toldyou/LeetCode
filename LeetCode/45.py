class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10000] * (len(nums))

        dp[0] = 0
        pq = []
        for i, num in enumerate(nums):
            while pq and -pq[0][1] < i:
                heapq.heappop(pq)

            if pq:
                dp[i] = min(dp[i], pq[0][0])

            heapq.heappush(pq, (dp[i]+1, -(i+num)))

        # print(dp)
        return dp[-1]
        
