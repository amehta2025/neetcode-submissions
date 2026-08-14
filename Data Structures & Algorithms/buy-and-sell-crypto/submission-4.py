class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l,r = 0,1
        for i in range(len(prices) - 1): 
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])

            r+=1
        
        return profit


#2 pointers, 0 and 1. right++ and left = right when prices[l] > prices[r]
        