class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)

        def getVal(idx: int) -> int:
            if idx < 0:
                return -(2**32)
            if idx >= n*m:
                return 2**32
            col = idx % n
            row = (idx-col) // n
            return matrix[row][col]

        low = -1
        high = n * m - 1
        while low+1 < high:
            mid = low + (high-low) // 2
            if getVal(mid) == target:
                return True
            elif getVal(mid-1) < target and getVal(mid+1) > target:
                return False
            
            if getVal(mid) < target:
                low = mid
            else:
                high = mid
        return getVal(high) == target
