class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if grid[r][c] != 1: #if water or visited
                return 0
            
            grid[r][c] = 2 # or back to water i.e 0

            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs (r, c+1) + dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area

        # TC and SC: O(rows · cols)
            








        