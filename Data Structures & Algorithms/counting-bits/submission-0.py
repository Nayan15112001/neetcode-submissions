class Solution:
    def countBits(self, n: int) -> List[int]:
        res =[]
        def count1(num):
            count = 0
            for c in num:
                if c == '1':
                    count+=1
            return count
            

        for i in range(n+1):
            count = count1(bin(i)[2:])
            res.append(count)

        return res
