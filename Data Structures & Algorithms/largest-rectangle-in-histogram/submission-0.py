class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        res = []
        for i in range(n):
            l,r = i,i
            while l>0: 
                if heights[l-1]>=heights[i]:
                    l-=1
                else:
                    break
            while r<n-1:
                if heights[r+1]>=heights[i]:
                    r+=1
                else:
                    break
            stk.append([l,r])
        print(stk)
        for i in range(n):
            l = stk[i][0]
            r = stk[i][1]
            area = (r-l+1)*heights[i]
            res.append(area)
        print(res)
        return max(res)


