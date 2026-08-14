class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maximum = 1
        numSet = set(nums)
        for i in nums:
            if i+1 in numSet and i-1 not in numSet:
                j= i
                temp = 0
                while (j in numSet):
                    temp+=1
                    j+=1
                maximum = max(temp, maximum)
        
        return maximum


    #for each value in nums, if value +1 is there AND value -1 is there, thats a start