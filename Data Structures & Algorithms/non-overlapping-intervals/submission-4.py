class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])        
        print(intervals)
        n = len(intervals)
        i = 0
        count = 0
        while i<n:
            start = intervals[i][0]
            end = intervals[i][1]
            while i<n-1 and intervals[i+1][0]<end:
                count+=1
                i+=1    
            i+=1    
        return count