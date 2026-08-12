class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        map = {")" : "(", "]" : "[", "}" : "{"}
        for i in s:
            if i in map:
                if not list1 or list1[len(list1)-1] != map[i]:
                    return False;
                list1.pop()
            else:
                list1.append(i)
        return not list1;
                

#make a stack, map with the mapping closed to opened
#no such thing as a char in python
#return when list is empty --> all openers had associated closers