class Solution:
    def solve(self, board: List[List[str]]) -> None:
        deltas = [[0,1], [0,-1], [1,0], [-1,0]]
        m, n = len(board), len(board[0])
        queue = collections.deque()
        safe = set()
        visited = set()

        for r in range(m):
            for c in range(n):
                if r == 0 or r == m-1 or c == 0 or c == n-1:
                    if board[r][c] == 'O':
                        queue.append((r,c))

        while queue:
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()
                if (r,c) not in visited and r >= 0 and c >= 0 and r < m and c < n and board[r][c] == 'O':
                    safe.add((r,c))
                    for delta in deltas:
                        queue.append((r + delta[0], c + delta[1]))
                visited.add((r,c))
        
        for r in range(m):
            for c in range(n):
                if (r,c) not in safe:
                    board[r][c] = 'X'