class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []   #initializing prefix array 
        currSum = 0
        for n in nums:
            currSum+=n
            self.prefix.append(currSum)
        

    def sumRange(self, left: int, right: int) -> int:
        compare = 0
        if left != 0:
            compare = self.prefix[left-1]
        
        return self.prefix[right] - compare
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)