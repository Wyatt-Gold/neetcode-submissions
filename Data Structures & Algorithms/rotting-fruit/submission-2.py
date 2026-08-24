from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        queue = deque()
        fresh_oranges = 0

        # Find all starting rotten oranges and count fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        minutes = 0

        # Continue while there are oranges that can spread rot
        while queue and fresh_oranges > 0:
            # Process one "minute" worth of oranges
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    new_r = r + dr
                    new_c = c + dc

                    # Check bounds and make sure the orange is fresh
                    if (
                        new_r < 0 or new_c < 0 or
                        new_r >= ROWS or new_c >= COLS or
                        grid[new_r][new_c] != 1
                    ):
                        continue

                    # Rot the orange and add it for the next BFS level
                    grid[new_r][new_c] = 2
                    fresh_oranges -= 1
                    queue.append((new_r, new_c))

            minutes += 1

        return minutes if fresh_oranges == 0 else -1