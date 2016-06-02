

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

442 ms
100% test cases passed.
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        intervals.sort( key = lambda x: x.start)
        i = 0
        while i < len(intervals):
            if (i + 1) < len(intervals) and intervals[i].end >= intervals[i+1].start:
                intervals[i].end = max(intervals[i].end, intervals[i+1].end)
                del intervals[i+1]
            else:
                i += 1
        return intervals
                