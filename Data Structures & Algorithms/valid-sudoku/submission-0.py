from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        #squares is gonna store keys as follows
        #there are gonna be 9 total squares: all combinations of 0,1,2
        #the key when we're in the for loop is gonna be (row // 3, col//3)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i] 
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[(i//3,j//3)]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])
        
        return True


