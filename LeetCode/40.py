class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # freqs = Counter(candidates)
        # candidates = []
        # for val, freq in freqs.items():
        #     for i in range(min(freq, math.ceil(30/val))):
        #         candidates.append(val)

        n = len(candidates)
        candidates.sort()
        ans = []

        def bt(i: int, combo: List[int], accu: int):
            if accu > target:
                return
            if accu == target:
                ans.append([*combo])
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                combo.append(candidates[j])
                bt(j+1, combo, accu+candidates[j])
                combo.pop()

        bt(0, [], 0)

        return ans