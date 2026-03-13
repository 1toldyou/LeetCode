class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        segments = []
        seg = []
        for num in nums:
            if num == 0:
                if len(seg) > 0:
                    segments.append(seg)
                    seg = []
            else:
                seg.append(num)
        segments.append(seg)
        
        for segment in segments:
            negs = 0
            firstNeg = -1
            lastNeg = -1
            for i, num in enumerate(segment):
                if num < 0:
                    negs += 1
                    if firstNeg == -1:
                        firstNeg = i
                    lastNeg = i
            if negs % 2 == 0:
                ans = max(ans, len(segment))
            else:
                ans = max(ans, len(segment)-firstNeg-1, lastNeg)
    
        return ans