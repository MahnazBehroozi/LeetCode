class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)>0:
            buy = prices[0]
            profit = 0
            for i in range(1,len(prices)):
                sell = prices[i]
                if sell-buy>profit:
                    profit= sell-buy
                if prices[i]<buy:
                    buy = prices[i]
                    
            return profit
        else:    
            return 0
