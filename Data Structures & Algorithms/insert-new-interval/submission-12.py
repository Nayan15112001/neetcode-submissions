class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        i = 0
        while i<n:
            if intervals[i][0]<newInterval[0] and intervals[i][1]<newInterval[0]:
                start = intervals[i][0]
                end = intervals[i][1]
            elif intervals[i][0]>newInterval[1] and intervals[i][1]>newInterval[1]:
                start = newInterval[0]
                end = newInterval[1]
                newInterval = [float('inf'),float('inf')]
            else:
                start = min(intervals[i][0],newInterval[0])
                end = max(intervals[i][1],newInterval[1])
                newInterval = [float('inf'),float('inf')]
            while i<n and end >= intervals[i][0]:
                end = max(end,intervals[i][1])
                i+=1
            ans.append([start,end])     

        if newInterval != [float('inf'),float('inf')]:
            ans.append(newInterval)

        return ans
