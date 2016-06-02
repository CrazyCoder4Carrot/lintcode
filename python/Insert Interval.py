"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        intervals.append(newInterval)
        intervals.sort( key = lambda x: x.start)
        i = 0
        while i < len(intervals):
            if (i + 1) < len(intervals) and intervals[i].end >= intervals[i+1].start:
                intervals[i].end = max(intervals[i].end, intervals[i+1].end)
                del intervals[i+1]
            else:
                i += 1
        return intervals