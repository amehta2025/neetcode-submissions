class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0

        for c in charSet:  #we just want to traverse the chars 
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == c:  #if you find a character that's c, inc count
                    count+=1

                while(r - l + 1) - count > k:     #while #elements - count of c > k, dec till reach k because you want to eventually reach a substring where you only need to change K CHARACTERS for the string to have just 1 character
                    if (s[l] == c):
                        count-=1     #if the left value is c, you're removing 1 from count
                    l+=1
                
                res = max(res, r - l + 1)
        return res
                      
                
            