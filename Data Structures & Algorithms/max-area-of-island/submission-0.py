class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        maxArea = 0
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])
        deltas = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0
            
            res = 1
            visited.add((r, c))
            for dr, dc in deltas:
                res += dfs(r + dr, c + dc)
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea