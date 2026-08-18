class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = []
        sum = 0
        for i in nums:
            sum += i
            pref.append(sum)
        
        for i in range(len(pref)):
            left = 0
            right = pref[-1] - pref[i]
            if i > 0:
                left = pref[i-1]
            if (right == left):
                return i

        return -1