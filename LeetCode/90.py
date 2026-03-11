class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        def bt(start: int, combo: List[int]):
            ans.append([*combo])

            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                combo.append(nums[i])
                bt(i+1, combo)
                combo.pop()
        
        bt(0, [])

        return ans
        