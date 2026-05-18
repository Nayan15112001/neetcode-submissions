class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        for i in range(len(matrix)):
            l = 0
            r = n-1
            while l<=r:
                m = l + ((r-l)//2)
                print(matrix[i][m])
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m]<target:                    
                    l = m+1
                else:
                    r = m-1
        return False