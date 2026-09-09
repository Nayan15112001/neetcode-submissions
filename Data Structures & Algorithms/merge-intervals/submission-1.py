class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 0
        ans = []
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            while i<n and end >= intervals[i][0]:
                end = max(end,intervals[i][1])
                i+=1
            ans.append([start,end])

        return ans
        