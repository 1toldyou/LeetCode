class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxRange = 0
        for i, num in enumerate(nums):
            if i > maxRange:
                return False
            maxRange = max(maxRange, i+num)
        return True
        