class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        n = len(intervals)
        i = 0
        if n == 0:
            if newInterval:
                ans.append(newInterval)
                return ans
            else:
                return []
        while i<n:
            if intervals[i][0]<=newInterval[0]<=intervals[i][1]:
                temp = [intervals[i][0],max(intervals[i][1],newInterval[1])]
                newInterval = [float('inf'),float('inf')]
            elif intervals[i][0]<=newInterval[1]<=intervals[i][1]:
                temp = [min(intervals[i][0],newInterval[0]),intervals[i][1]]
                newInterval = [float('inf'),float('inf')]
            elif (newInterval[0]<intervals[i][0] and newInterval[1]<intervals[i][0]) or (newInterval[0]<intervals[i][0] and intervals[i][1]<newInterval[1]) :
                temp = newInterval
                newInterval = [float('inf'),float('inf')]
            else:
                temp = intervals[i]
            end = temp[1]
            while i<n and end >= intervals[i][0]:
                end = max(end,intervals[i][1])
                i+=1
            temp[1] = end
            ans.append(temp)     

        if newInterval != [float('inf'),float('inf')]:
            ans.append(newInterval)

        return ans
