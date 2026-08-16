class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) #only add the interval at i, dont return YET

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)  #you wanna add the newinterval at the end because if you've gotten here, that means that newInterval hasn't been added yet
        return res



    

    #if new interval end is less than curr interval start, add new interval, followed by the rest of the 2darray

#if new interval start is greater than current interval end
#else: new interval is overlapping. take minimum of both intervals for start and max for end