class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)

        a = 0
        b = 0
        while a < n and b < n:
            if height[a] == 0:
                a += 1
                continue
            
            pq = []
            b = a + 1
            while b < n:
                if height[b] >= height[a]:
                    break
                heapq.heappush(pq, (-height[b], b))
                b += 1
            # print("a", a, "b", b)
            if b < n:  # find wall before the end
                x = b-a - 1
                if x == 0:
                    a = b
                    continue
                area = x * min(height[a], height[b])
                for i in range(a+1, b):
                    area -= height[i]
                ans += area
                # print("a", a, "b", b, "area", area)
                a = b
            else:
                while pq:
                    candidate = heapq.heappop(pq)
                    if candidate[1] <= a+1:  # before and the one right after
                        # print("might be another wall", candidate[1])
                        a = max(a, candidate[1])
                        continue
                    b = candidate[1]
                    area = (b-a-1) * min(height[a], height[b])
                    for i in range(a+1, b):
                        area -= height[i]
                    ans += area
                    # print("a", a, "b", b, "area", area)
                    a = b
                
        return ans
        
