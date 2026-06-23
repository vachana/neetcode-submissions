class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: #check empty grid for edge case
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r,c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] != "1": #if water or visited
                return 
            
            grid[r][c] = "#" #masrk as visited

            dfs(r-1, c) or dfs(r+1, c) or dfs (r, c+1) or dfs(r, c-1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count +=1
                    dfs(r,c)

        return count


        # TC : O(rows · cols)
        # Every cell is visited at most once — once marked # it's never processed again. So the total work across all DFS calls is proportional to the number of cells.
        # SC O(rows · cols)
        # Worst case the entire grid is land and the recursion stack goes rows·cols levels deep — one frame per cell in the DFS chain.