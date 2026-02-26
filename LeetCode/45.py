class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10000000] * (n)

        dp[0] = 0
        pq = []
        for i, num in enumerate(nums):
            while pq and -pq[0][1] < i:
                heapq.heappop(pq)
                # print("invalidate", heapq.heappop(pq))

            if pq:
                dp[i] = min(dp[i], pq[0][0])

            nextIdx = min(i+num, n-1)
            heapq.heappush(pq, (dp[i]+1, -nextIdx))

            dp[nextIdx] = min(dp[nextIdx], dp[i] + 1)
            # print(f"nums[{i}]={num} dp[{i}]={dp[i]} pq={pq[:3]}")

        # print(dp)
        return dp[-1]
        
