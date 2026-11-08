class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        def dfs(temp):
            if len(temp) == len(nums):
                res.append(temp.copy())
            
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(temp)
                temp.pop()
        
        dfs([])
        return res