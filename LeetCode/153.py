class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        low = 0
        high = n-1
        while low+1 < high:
            mid = low + (high-low)//2
            # print(f"low={low} high={high} mid={mid}")

            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] > nums[-1]:
                low = mid
            else:
                high = mid
        
        return nums[high]

        