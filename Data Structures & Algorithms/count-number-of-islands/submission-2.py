class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):  #let's create a queue
            q = collections.deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:  #generally always how you write bfs
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr >= ROWS or nc >= COLS or nr <0 or nc < 0 or grid[nr][nc] =="0"):
                        continue;
                    q.append((nr, nc))
                    grid[nr][nc] = "0"


        #notice how this part is identical to the dfs solution
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1

        return islands