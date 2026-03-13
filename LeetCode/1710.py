class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        # print(boxTypes)
        ans = 0
        for boxType in boxTypes:
            ans += boxType[1] * min(boxType[0], truckSize)
            truckSize -= boxType[0]
            if truckSize <= 0:
                break
        return ans