class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        dp = [0] * n
        lowest = 2**32
        highest = -(2**32)
        gasSum = 0
        costSum = 0
        possibleStartIdx = []
        for i in range(n):
            gasSum += gas[i]
            costSum += cost[i]
            dp[i] = gas[i] - cost[i]
            if dp[i] > 0:
                possibleStartIdx.append(i)
            if i > 0:
                dp[i] += dp[i-1]
            lowest = min(lowest, dp[i])
            highest = max(highest, dp[i])

        if costSum > gasSum:
            return -1

        if highest < 0:
            return -1

        if n == 1:
            return 0

        for i in possibleStartIdx:
            if gas[i] > cost[i]:
                if gas[i] - cost[i] - dp[i] + lowest >= 0:
                    return i
        
        return -1
        