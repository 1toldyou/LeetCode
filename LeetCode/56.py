class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)

        n = len(intervals)
        res = []
        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        for i in range(1, n):
            curr = intervals[i]
            if curr[0] <= prevEnd:
                prevEnd = max(prevEnd, curr[1])
            else:
                res.append([prevStart, prevEnd])
                prevStart = curr[0]
                prevEnd = curr[1]

        res.append([prevStart, prevEnd])

        return res        
