class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj: List[List[Tuple[int, int]]] = [[] for i in range(n)]
        for i in range(n):
            curr = points[i]
            for j in range(n):
                if i == j:
                    continue
                neighbor = points[j]
                dist = abs(curr[0] - neighbor[0]) + abs(curr[1] - neighbor[1])
                adj[i].append((dist, j))
            heapq.heapify(adj[i])
        # print(adj)

        visited = set()
        visited.add(0)
        ans = 0
        while len(visited) < n:
            minCost = 2**32
            minIdx = -1
            for node in visited:
                while adj[node] and adj[node][0][1] in visited:
                    heapq.heappop(adj[node])
                if len(adj[node]) == 0:
                    continue
                if adj[node][0][0] <= minCost:
                   minCost = adj[node][0][0]
                   minIdx = node
            nextNode = heapq.heappop(adj[minIdx])
            visited.add(nextNode[1])
            ans += minCost
        return ans