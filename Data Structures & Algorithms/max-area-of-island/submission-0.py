class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r >= ROWS or c >= COLS or c < 0 or r < 0 or grid[r][c] == 0:
                return 0;  #contribute nothing
            
            grid[r][c] = 0
            add = 1  #count myself

            for dr, dc in directions:
                add += dfs(r + dr, c + dc) #add what each neighbor found
            return add
                


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res


# general algorithm: dfs through graph, find all things connected, make sure to increment when find more land