class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,temp):
            if i>=len(nums):
                res.append(temp.copy())
                return
    
            temp.append(nums[i])
            dfs(i+1, temp)
            temp.pop()
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,temp)
        
        dfs(0,[])
        return res
            

            
            