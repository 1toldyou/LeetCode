class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        insStart = newInterval[0]
        insEnd = newInterval[1]
        for interval in intervals:
            if interval[1] < insStart:  # before 
                res.append(interval)
            elif interval[0] <= insEnd:
                insStart = min(insStart, interval[0])
                insEnd = max(insEnd, interval[1])
            else:
                res.append(interval)
        res.append([insStart, insEnd])

        return sorted(res)
        