class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i,j=0,0
        #traversing row wise
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s and board[i][j]!= ".":
                    return False
                else:
                    s.add(board[i][j])
        print("rows succeeded")
        #traversing col wise
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s and board[j][i]!= ".":
                    return False
                else:
                    s.add(board[j][i])
                    
            
        print("cols succeeded")

        #traversing 3x3 boxes
        for r in range(0,9,3):
            for c in range(0,9,3):
                s = set()
                # print(f"box {r}{c}")
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        # print(f"i:{i} j:{j} ------> {board[i][j]}")
                        # print(s)
                        if board[i][j] in s and board[i][j]!= ".":
                            return False
                        else:
                            s.add(board[i][j])
        print("boxes succeeded")

        return True

    
         