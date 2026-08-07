class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in nums:
                    return False
                if board[row][col] != '.':
                    nums.add(board[row][col])
            nums = set()
        
        nums = set()
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] in nums:
                    return False
                if board[row][col] != '.':
                    nums.add(board[row][col])
            nums = set()

        for square in range(9):
            nums = set()
            rowOff = (square // 3) * 3
            colOff = (square % 3) * 3
            for row in range(len(board)//3):
                for col in range(len(board[0])//3):
                    if board[row+rowOff][col+colOff] in nums:
                        return False
                    if board[row+rowOff][col+colOff] != '.':
                        nums.add(board[row+rowOff][col+colOff])
            

        return True