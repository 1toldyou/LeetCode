class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        a = 0
        b = n-1

        while a < b:
            curr = numbers[a] + numbers[b]
            if curr == target:
                break
            elif curr > target:
                b -= 1
            else:
                a += 1

        return [a+1, b+1]