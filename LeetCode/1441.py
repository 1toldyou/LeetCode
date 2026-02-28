class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        stack = []
        x = 0            

        for i, num in enumerate(target):
            if not stack:
                x += 1
                stack.append(x)
                ans.append("Push")
            while stack[-1] != num:
                if stack[-1] != target[i-1]:
                    stack.pop()
                    ans.append("Pop")
                x += 1
                stack.append(x)
                ans.append("Push")

        return ans