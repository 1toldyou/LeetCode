class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = [2**32] * 26
        last = [-(2**32)] * 26

        def char2int(c: str) -> int:
            return ord(c) - ord("a")

        for i, c in enumerate(s):
            first[char2int(c)] = min(first[char2int(c)], i)
            last[char2int(c)] = max(last[char2int(c)], i)

        intervals = []
        for i in range(26):
            if first[i] <= 500 and last[i] >= 0:
                intervals.append((first[i], last[i]))
        intervals.sort()

        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        intervals.pop(0)
        for interval in intervals:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                ans.append(end-start+1)
                start = interval[0]
                end = interval[1]
        ans.append(end-start+1)

        return ans