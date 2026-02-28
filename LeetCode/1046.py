class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-1 * stone for stone in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            # print(pq)
            y = heapq.heappop(pq) * -1
            x = heapq.heappop(pq) * -1
            if x == y:
                continue
            else:
                heapq.heappush(pq, -(y - x))
                
        return (pq[0] * -1) if len(pq) == 1 else 0