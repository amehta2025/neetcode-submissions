class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1 = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            max1 = max(max1, r-l + 1)
            r+=1
        
        return max1




#2 pointers 0,1.. update r everytime new character is introduced
#longest = l - r
#definitely review this ebcause i suck and can't find solution