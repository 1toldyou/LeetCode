class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        ans = 0

        DX = [-1, 1, 0, 0]
        DY = [0, 0, -1, 1]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    area = 0
                    grid[row][col] = 2
                    curr = [(row, col)]
                    while curr:
                        nextLayer = []
                        for r, c in curr:
                            area += 1
                            for i in range(4):
                                nR = r + DY[i]
                                nC = c + DX[i]
                                if nR < 0 or nR >= m or nC < 0 or nC >= n:
                                    continue
                                if grid[nR][nC] != 1:
                                    continue
                                nextLayer.append((nR, nC)) 
                                grid[nR][nC] = 2
                        curr = nextLayer
                    ans = max(ans, area)
        
        return ans
        