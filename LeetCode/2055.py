class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        plates = [0] * n
        leftCandles = [-1] * n
        rightCandles = [-1] * n

        accu = 0
        for i, c in enumerate(s):
            accu = accu + (1 if c == "*" else 0)
            plates[i] = accu
        # print("plates", plates)

        prev = -1
        for i, c in enumerate(s):
            if c == "|":
                prev = i
                leftCandles[i] = i
            else:
                leftCandles[i] = prev
        # print("leftCandles", leftCandles)

        nextCandle = n
        for i in range(n-1, -1, -1):
            if s[i] == "|":
                nextCandle = i
                rightCandles[i] = i
            else:
                rightCandles[i] = nextCandle
        # print("rightCandles", rightCandles)

        ans = []
        for query in queries:
            leftBound = rightCandles[query[0]]
            rightBound = leftCandles[query[1]]
            # print("query", query, "leftBound", leftBound, "rightBound", rightBound)
            if leftBound <= query[1] and rightBound >= query[0]:
                ans.append(plates[rightBound] - plates[max(0, leftBound-1)])
            else:
                ans.append(0)
        return ans