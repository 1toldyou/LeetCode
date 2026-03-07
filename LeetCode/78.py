class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        def bt(i: int, combo: List[int]):
            ans.append(list(combo))
            for j in range(i, n):
                combo.append(nums[j])
                bt(j+1, combo)
                combo.pop()
        
        bt(0, [])
        return ans