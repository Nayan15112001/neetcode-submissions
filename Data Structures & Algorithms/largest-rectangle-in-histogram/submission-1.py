class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        res = []
        maxarea =0
        for i in range(n):
            index = i
            while stk and heights[i]<=stk[-1][1]:
                area = (i-stk[-1][0])*stk[-1][1]
                maxarea = max(maxarea,area)
                index,val = stk.pop()
            stk.append([index,heights[i]])
        print(stk)
        for i in range(len(stk)):
            l = stk[i][0]
            r = n-1
            area = (r-l+1)*stk[i][1]
            maxarea = max(maxarea,area)
        return maxarea


