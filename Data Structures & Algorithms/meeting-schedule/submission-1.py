"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n =  len(intervals)
        i = 0
        prev_end = None
        heap = []
        def heap_sort(intervals):
            for interval in intervals:
                heapq.heappush(heap,[interval.start,interval.end])
        heap_sort(intervals)
        while heap:
            start,end = heapq.heappop(heap)
            print(start,end)            
            if prev_end and start<prev_end:
                return False
            prev_end = end 


        return True
