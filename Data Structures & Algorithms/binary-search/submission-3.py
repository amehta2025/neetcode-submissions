class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums) -1
        while(i <= j):
            middle = int((i + j) /2)
            if nums[middle] < target:
                i = middle+1
            elif nums[middle] > target:
                j=middle-1
            else:
                return middle
            
        return -1
    


# another way to prevent integer overflow: a + (b-a)/2
#python doesn't do integer division
