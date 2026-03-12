class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        n = len(intervals)
        
        intervals.sort(key=lambda p: (p[1], p[0]))
        # print(intervals)

        prevEnd = intervals[0][1]
        intervals.pop(0)
        for interval in intervals:
            if interval[0] < prevEnd:
                # print("removing", interval)
                ans += 1
            else:
                prevEnd = interval[1]

        return ans
