class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i, a in enumerate(nums):
            map1[a] = i

        for i in range(len(nums)):
            total = target - nums[i]
            if total in nums and i != map1[total]:
                return [i, map1[total]]
        
        return []

        