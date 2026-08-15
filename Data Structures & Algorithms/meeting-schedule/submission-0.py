"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start) #this is an inline function

        for i in range(len(intervals) -1):
            i1 = intervals[i]
            i2 = intervals[i+1]
            if i2.start < i1.end:
                return False
        
        return True



#brute force,
#sort by start time (remember that intervals is an object), see if the next meeting starts before the previous meeting ended