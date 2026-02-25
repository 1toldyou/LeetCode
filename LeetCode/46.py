class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def bt(combo: List[int], used: List[bool]):
            if len(combo) == len(nums):
                res.append([*combo])
            for i, num in enumerate(nums):
                if used[i] is False:
                    combo.append(num)
                    used[i] = True
                    bt(combo, used)
                    used[i] = False
                    combo.pop()
        
        bt([], [False for num in nums])

        return res
        
