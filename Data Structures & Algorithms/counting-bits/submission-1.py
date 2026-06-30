class Solution:
    def countBits(self, n: int) -> List[int]:
        res =[]
        def count1(num):
            count = 0
            while num>0:
                if num%2 == 1:
                    count+=1
                num//=2
            return count
            

        for i in range(n+1):
            count = count1(i)
            res.append(count)

        return res
