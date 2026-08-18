class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max1 = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet: #while it's in charSet, keep removing from left until its gone
                charSet.remove(s[l])
                l+=1              #this keeps the charSet start aligned with the string
            charSet.add(s[r])
            max1 = max(max1, r - l + 1)  #max of curr max and the current substring length (r - l + 1)
        
        return max1
