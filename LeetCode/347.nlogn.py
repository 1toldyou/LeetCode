class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_list = [(-v, k) for k, v in freqs.items()]
        heapq.heapify(freqs_list)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(freqs_list)[1])
        return ans