class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0]) #sort by start value
        res = [intervals[0]] #on't declare it empty; declare after sort so you always get min value for res[-1][0]
        for start, end in intervals:
            lastE = res[-1][1]  #end value of most recent output
            if start <= lastE:  #if overlap
                res[-1][1] = max(lastE, end)
            else:
                res.append([start, end])    #make sure to add to a 2d list, add as [ , ]
                
        return res


# if intervals are processed in sorted order by start time, then any overlap can only happen with the most recently added interval