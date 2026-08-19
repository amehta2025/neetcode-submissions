class Solution: #make sure can recognize now
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #contains pairs   (val, index)
        for index, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                stackVal, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append((val, index ))
        
        return res



#use monotonically decreasing stack
#stack contains pair of values, (val, idx)