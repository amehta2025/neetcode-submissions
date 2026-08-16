class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        
        return one



#dynamic programming is solving complex problems by breaking them down into simpler problems
#top down (memoization) --> break a problem down recursively
#bottom up (tabulation) --> starts from base cases and works its way to final solution
# (caching) means storing the result so you can use it next time instead of calculating the same thing again and again
#store memory of smaller subproblems in dp