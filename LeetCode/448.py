class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n+1)
        for num in nums:
            freq[num] += 1
        
        ans = []
        for i in range(1, n+1):
            if freq[i] == 0:
                ans.append(i)
        return ans