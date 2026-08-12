class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:  #self is the first method of any method in a class
    #self is always gonna be there, ignore it. 
    #passes nums, which is a list and you return a bool. this is all just documentaiton
        s1 = set()
        for i in nums:
            s1.add(i)
        return len(s1) != len(nums)