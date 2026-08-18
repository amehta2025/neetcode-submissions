class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))  #remember to use self.helper
        #first argument skips 1st index, last argument skips last index (-1)

    def helper(self, nums):
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]


#the whole premise of this is that you want to calculate the max of dp in 2 ways
#one way skips first element, second way skips last element (-1)