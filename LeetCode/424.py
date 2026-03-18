class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        A = ord("A")
        n = len(s)
        ans = 0
        freq = [0] * 26
        a = -1
        b = 0
        while b < n:
            freq[ord(s[b])-A] += 1
            while (b - a) > max(freq) + k:
                a += 1
                freq[ord(s[a])-A] -= 1
            ans = max(ans, b - a)
            b += 1 

        return ans
        