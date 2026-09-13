"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heap = []
        ans = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            print(start,end)
            if heap and start>=heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
            ans = max(ans,len(heap))
        return ans
                

