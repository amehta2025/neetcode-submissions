class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  #n XOR 0 = n
        for n in nums:
            res = n ^ res
        return res

#XOR  --> if two bits are the exact same,  1 XOR 1 = 0, 
#XOR can be done in any order
#res = 0 ^ 4       # 4
#res = 4 ^ 1       # 5
#res = 5 ^ 2       # 7
#res = 7 ^ 1       # 6
#res = 6 ^ 2       # 4