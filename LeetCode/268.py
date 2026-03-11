class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        zeroFound = False
        nonZero = 0

        for num in nums:
            if num == 0:
                zeroFound = True
            else:
                nonZero = num

        if not zeroFound:
            return 0
        if nonZero == 0:
            return 1

        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = nonZero

        for num in nums:
            num = abs(num)
            nums[num-1] = -abs(nums[num-1])

        for i, num in enumerate(nums):
            if num > 0:
                return i+1

        return False

        