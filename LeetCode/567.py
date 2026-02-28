class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m < n:
            return False
        s1Freq = {}
        s2Freq = {}

        def same():
            for k, v in s1Freq.items():
                if v != s2Freq.get(k):
                    return False
            return True

        for c in s1:
            if not s1Freq.get(c):
                s1Freq[c] = 0
            s1Freq[c] += 1

        a = -1
        b = -1
        for i in range(n):
            b += 1
            c = s2[b]
            if not s2Freq.get(c):
                s2Freq[c] = 0
            s2Freq[c] += 1

        if same():
            return True

        for i in range(n, m):
            b += 1
            c = s2[b]
            if not s2Freq.get(c):
                s2Freq[c] = 0
            s2Freq[c] += 1

            a += 1
            s2Freq[s2[a]] -= 1

            if same():
                return True

        return False
