class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        highest = 0
        for price in prices:
            low = min(low, price)
            highest = max(highest, price-low)
    
        return highest
        