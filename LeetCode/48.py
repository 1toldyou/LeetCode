class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2):
            upLeft= (layer, layer)
            upRight = (layer, n-layer-1)
            downLeft= (n-layer-1, layer)
            downRight = (n-layer-1, n-layer-1)
            width = n - layer*2
            # print(upLeft, upRight, downLeft, downRight, width)

            temp = [*matrix[upLeft[0]][upLeft[1]:upRight[1]+1]]
            # print(temp)
            for row in range(width):  # left side
                matrix[upLeft[0]][upRight[1]-row] = matrix[upLeft[0]+row][upLeft[1]]
            for col in range(width):  # down side
                matrix[upLeft[0]+col][upLeft[1]] = matrix[downLeft[0]][downLeft[1]+col]
            for row in range(width):  # right side
                matrix[downLeft[0]][downLeft[1]+row] = matrix[downRight[0]-row][downRight[1]]
            for col in range(width):  # top side
                matrix[upRight[0]+col][upRight[1]] = temp[col]