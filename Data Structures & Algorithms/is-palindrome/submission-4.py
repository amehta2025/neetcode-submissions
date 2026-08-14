class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i+=1
                j-=1
            
        return True

#2 pointers in front and back. keep going, ignore stuff that isn't alnum, compare
#don't forget to compare with tolower