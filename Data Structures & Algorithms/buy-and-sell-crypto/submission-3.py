class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,maxi = 0,1,0

        for _ in range(len(prices) -1):
            if prices[l] >= prices[r]:
                l = r
            else:
                maxi = max(prices[r]-prices[l], maxi)
            r+=1;
        return maxi
        
        


#2 pointers, right pointer traverses for loops
#max, max updates when new max
#left pointer equals right pointer when left > right