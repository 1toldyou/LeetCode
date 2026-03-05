class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [2**32] * (n+1)
        adj = [[] for i in range(n+1)]

        for edge in times:
            adj[edge[0]].append((edge[1], edge[2]))

        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))
        while pq:
            cost, curr = heapq.heappop(pq)

            if cost > dist[curr]:
                continue

            for edge in adj[curr]:
                if cost+edge[1] < dist[edge[0]]:
                    dist[edge[0]] = cost+edge[1]
                    heapq.heappush(pq, (dist[edge[0]], edge[0]))

        maxDist = max(dist[1:])
        return -1 if maxDist == 2**32 else maxDist 
        