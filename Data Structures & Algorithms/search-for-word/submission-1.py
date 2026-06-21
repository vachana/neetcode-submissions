class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] == "#":
                return False
            if board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            exists = dfs(r+1,c, index+1) or dfs(r-1,c, index+1) or dfs(r, c+1, index+1) or dfs(r, c-1, index+1)

            board[r][c] = temp 

            return exists

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

# TC: O(rows · cols · 4^w), w->length of the word (4->4 directions of dfs)
# SC: O(w)
# Recursion stack goes at most w levels deep — one level per character matched.
# No extra space for visited since you're using the # trick in place.


            