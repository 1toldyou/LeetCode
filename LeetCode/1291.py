class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        def bt(s: str):
            num = int(s)
            if num > high:
                return
            if num >= low:
                ans.append(num)
            lastDigit = int(s[-1])
            if lastDigit < 9:
                bt(s+str(lastDigit+1))

        for i in range(1, 10):
            bt(str(i))

        ans.sort()

        return ans