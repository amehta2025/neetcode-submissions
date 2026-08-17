class Solution:
    def climbStairs(self, n: int) -> int:
        if (n < 2):
            return n
        dp = [0] * (n+ 1) #because you also want a space for the 0th element
        dp[1], dp[2] = 1, 2 #setting base cases for the dp
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]



#dynamic programming is solving complex problems by breaking them down into simpler problems
#top down (memoization) --> break a problem down recursively
#bottom up (tabulation) --> starts from base cases and works its way to final solution
# (caching) means storing the result so you can use it next time instead of calculating the same thing again and again
#store memory of smaller subproblems in dp