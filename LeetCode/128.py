class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = {}
        for num in nums:
            unique[num] = True
        
        heads = []
        for k, v in unique.items():
            if unique.get(k-1) is None:
                heads.append(k)

        ans = 0
        for head in heads:
            num = head
            while unique.get(num) is not None:
                num += 1
            ans = max(ans, num - head)
        
        return ans
