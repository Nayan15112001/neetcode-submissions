class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] *n
        stk = []
        for i,temp in enumerate(temperatures):
            while stk and temp>stk[-1][0]:
                val,index = stk.pop()
                res[index] = i-index
            stk.append([temp,i])
            

        return res
