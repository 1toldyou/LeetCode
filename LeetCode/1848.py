class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        bestVal = 2**32

        for i, num in enumerate(nums):
            if num != target:
                continue
            bestVal = min(bestVal, abs(i - start))

        return bestVal
        
