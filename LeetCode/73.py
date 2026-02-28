class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m = len(matrix)

        rows = [False] * m
        cols = [False] * n

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    rows[row] = True
                    cols[col] = True
        
        for row, work in enumerate(rows):
            if not work:
                continue
            for col in range(n):
                matrix[row][col] = 0
        for col, work in enumerate(cols):
            if not work:
                continue
            for row in range(m):
                matrix[row][col] = 0
        