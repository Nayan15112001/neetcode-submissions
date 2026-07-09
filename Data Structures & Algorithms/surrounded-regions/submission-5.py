from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        q = deque()

        for i in range(m):
            if board[i][0] == 'O' :
                board[i][0] = "#"
                q.append((i,0))
            if board[i][n-1] == 'O':
                board[i][n-1] = "#"
                q.append((i,n-1))

        for j in range(n):
            if board[0][j] == 'O' :
                board[0][j] = "#"
                q.append((0,j))
            if board[m-1][j] == 'O':
                board[m-1][j] = "#"
                q.append((m-1,j))


        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            
            r,c = q.popleft()

            for row,col in directions:
                nr = r+row
                nc = c+col

                if nr < 0 or nc<0 or nr>=m or nc>=n or board[nr][nc]!="O":
                    continue
                
                board[nr][nc] = "#"
                q.append((nr,nc))
        print(board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != "#":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"

