class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        for i in range(length):
            if(i == length-1):
                break            
            elif(prices[i] < prices[i+1]):
                profit += prices[i+1] - prices[i]
                i += 1
            else:
                i += 1
            
        return profit
