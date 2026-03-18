class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        ans = s[0]

        for i in range(1, n):
            # starts with one
            a = i
            b = i
            while a-1>= 0 and b+1<n and s[a-1] == s[b+1]:
                a -= 1
                b += 1
            # print(f"i={i} a={a} b={b}")
            if len(s[a:b+1]) > len(ans):
                ans = s[a:b+1]

            # starts with two
            a = i-1
            b = i
            if s[a] != s[b]:
                continue
            while a-1>= 0 and b+1<n and s[a-1] == s[b+1]:
                a -= 1
                b += 1
            # print(f"i={i} a={a} b={b}")
            if len(s[a:b+1]) > len(ans):
                ans = s[a:b+1]

        return ans 