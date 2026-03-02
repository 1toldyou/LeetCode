class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)

        segs1 = []
        negCounts = []
        seg = []
        negCount = 0
        for num in nums:
            if num != 0:
                seg.append(num)
                if num < 0:
                    negCount += 1
            else:
                segs1.append(seg)
                negCounts.append(negCount)
                seg = []
                negCount = 0
        if seg:
            segs1.append(seg)
            negCounts.append(negCount)

        segs2 = []
        for i, seg in enumerate(segs1):
            if len(seg) <= 1:
                continue
            if negCounts[i] % 2 == 0:
                ans = max(ans, math.prod(seg))
            else:
                a = 0
                b = len(seg)-1
                while seg[a] > 0:
                    a += 1
                while seg[b] > 0:
                    b -= 1
                left = math.prod(seg[:b])
                right = math.prod(seg[a+1:])
                if len(seg[:b]) == 0 and len(seg[a+1:]) == 0:
                    pass
                else:
                    ans = max(ans, left, right)

        return ans
        