class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        subs_grid_set = [set() for _ in range(9)]

        for row in range(rows):
            for col in range(cols):
                grid = (row // 3) * 3 + (col // 3)
                if (board[row][col] in rows_set[row]) or (board[row][col] in cols_set[col]) or (board[row][col] in subs_grid_set[grid]):
                    return False
                if board[row][col] != ".":
                    rows_set[row].add(board[row][col])
                    cols_set[col].add(board[row][col])
                    subs_grid_set[grid].add(board[row][col])
        
        return True

































        # row, col = len(board), len(board[0])

        # for i in range(row):
        #     temp = []
        #     for j in range(col):
        #         if board[i][j] not in [1,2,3,4,5,6,7,8,9,.] or board[i][j] in temp:
        #             return False
        #         temp.append(board[i][j])

        # for i in range(row):
        #     temp, x = [], 0
        #     for j in range(col):
        #         if 
        #         if board[i][j] not in [1,2,3,4,5,6,7,8,9,.] or board[i][j] in temp:
        #             return False
        #         temp.append(board[i][j])     
                
            