class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        freqs = Counter(nums)
        starts = sorted(list(freqs.keys()))
        # print(starts)
        for start in starts:
            while freqs[start] > 0:
                for i in range(k):
                    if not start+i in freqs or freqs[start+i] == 0:
                        return False
                    freqs[start+i] -= 1
        
        return True
