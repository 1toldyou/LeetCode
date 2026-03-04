class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        locs: List[List[int]] = [[] for i in range(101)]
        for i, temp in enumerate(temperatures):
            locs[temp].append(i)
        # print(locs)

        ans = []
        for i, temp in enumerate(temperatures):
            bestIdx = 2**32
            for j in range(temp+1, 101):
                # print(f"i={i} j={j}")
                while locs[j] and locs[j][0] <= i:
                    locs[j].pop(0)
                if locs[j] and locs[j][0] < bestIdx:
                    bestIdx = locs[j][0]
                if bestIdx == i+1:
                    break
            if bestIdx < n:  # found
                # print(f"{bestIdxTemp} > {temp}", f"in {bestIdx-i} days")
                ans.append(bestIdx-i)
            else:
                ans.append(0)
            # print(locs)
        
        return ans