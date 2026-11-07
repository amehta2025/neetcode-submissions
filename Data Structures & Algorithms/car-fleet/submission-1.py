#biggest advice for this one is like draw it out so you can better understand patterns and like also how it works in general
#sort pairs in increasing order based on position
#imagine an xy graph where x is time and y is position


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        stack = []
        arr.sort(reverse=True)
        for pos,sp in arr:
            if not stack:
                stack.append((pos,sp))
                continue
            
            pos2 = stack[-1][0]
            sp2 = stack[-1][1]
            time2 = (target - pos2) / sp2
            time1 = (target - pos) / sp

            if time1>time2:
                stack.append((pos,sp))
        
        return len(stack)



# 4 + 2t = 10
#1 + 2t = 10
