class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        for i in range(len(numbers)): #because r starts at 1
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total > target:
                r-=1
            else:
                l+=1
        return []
            

            
        

#nondecreasing = each element is equal to or greater than the previous
#creating a container that grows with input: extra O(n) space
#idea: create a two pointer, l+=1 always, r++++ till l + r > target --> no that O(n^2)
#solution: create pointers at start and end, if total too big, decrement r, if too small, dec l

        