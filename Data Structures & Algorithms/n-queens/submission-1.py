class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res =  []
        board = [["."]*n for _ in range(n)]

        def is_valid(row,col):
            count = 0 
            #col check
            for c in board[row]:
                if c == "Q":
                    count+=1
            
            if count>0:
                return False

            count = 0
            #row check
            for r in range(n):
                if board[r][col] == "Q":
                    count+=1
            if count>0:
                return False

            count = 0    
            #top right diagonal
            r,c = row,col
            while r>=0 and c<n:
                if board[r][c] == "Q":
                    count+=1
                r-=1
                c+=1
            if count>0:
                return False
            
            count = 0
            #top left diagonal
            r,c = row,col
            while r>=0 and c>=0:
                if board[r][c] == "Q":
                    count+=1
                r-=1
                c-=1
            if count>0:
                return False
            
            
            return True



        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n): 
                if not is_valid(row,col):
                    continue
                board[row][col] = "Q"
                backtrack(row+1)
                board[row][col] = "."

        backtrack(0)
        return res
        