class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        a = -1
        b = k-1

        nums = [-num for num in nums]

        freqs = {}
        window = nums[:k]
        for num in window:
            if freqs.get(num) is None:
                freqs[num] = 0
            freqs[num] += 1

        heapq.heapify(window)
        ans.append(-window[0])

        for i in range(k, n):
            b += 1
            a += 1
            newNum = nums[b]
            outNum = nums[a]
            if freqs.get(newNum) is None:
                freqs[newNum] = 0 
            freqs[newNum] += 1 
            freqs[outNum] -= 1
            heapq.heappush(window, newNum)            
            while window and freqs[window[0]] == 0:
                heapq.heappop(window)
            ans.append(-window[0])

        return ans