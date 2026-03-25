class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        levels = 0
        DX = [-1, 1, 0, 0]
        DY = [0, 0, -1, 1]

        curr = []
        hasOrange = False
        for row in range(m):
            for col in range(n):
                if grid[row][col] >= 1:
                    hasOrange = True
                if grid[row][col] == 2:
                    curr.append((row, col))

        if not hasOrange:
            return 0

        while curr:
            # print("curr", curr)
            levels += 1
            later = []
            for orange in curr:
                for i in range(4):
                    nR = orange[0] + DX[i]
                    nC = orange[1] + DY[i]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n:
                        continue
                    if grid[nR][nC] != 1:
                        continue
                    grid[nR][nC] = 2
                    later.append((nR, nC))
            curr = later

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1

        return levels - 1