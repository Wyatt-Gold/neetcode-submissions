class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        queue = collections.deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        curr_distance = 0
        while queue:
            length = len(queue)

            for _ in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if (
                        0 <= new_r < ROWS and
                        0 <= new_c < COLS and
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] != -1
                    ):
                        visited.add((new_r, new_c))
                        grid[new_r][new_c] = curr_distance + 1
                        queue.append((new_r, new_c))

            curr_distance += 1