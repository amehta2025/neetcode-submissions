class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1) #accounts for the 0 needed as first value; dp is the cost it took to get to a pos
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1): #iterate from 2 (first value that doesn't cost)
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[n]
        

        #For each, the cost is what it took to get there plus the price of leaving it:
        #cost is list of costs, dp is list of what it took to get you there