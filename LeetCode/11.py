class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        right = n-1
        while left < right:
            area = min(height[left], height[right]) * (right-left)
            ans = max(ans, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return ans
        