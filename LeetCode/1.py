class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}
        for i, num in enumerate(nums):
            diff = target - num
            if past.get(diff):
                return [past[diff][0], i]

            if not past.get(num):
                past[num] = []
            past[num].append(i)
        
        return []
        
