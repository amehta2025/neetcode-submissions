class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]: #essentially, have we already considered this value
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                threesum = val + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    if [val, nums[l], nums[r]] not in output:
                        output.append([val, nums[l], nums[r]])
                    l+=1
        
        return output




#constraints allow for an O(n^2) solution
#consider a similar process with two pointers like two sum 2
# :(. do this again when more confident
