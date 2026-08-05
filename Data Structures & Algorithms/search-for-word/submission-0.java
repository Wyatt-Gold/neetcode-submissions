class Solution {
    public boolean exist(char[][] board, String word) {
        int[][] visited = new int[board.length][board[0].length];

        for(int r = 0; r < board.length; r++){
            for(int c = 0; c < board[r].length; c++){
                if(helper(board, word, r, c, visited)){
                    return true;
                }
            }
        }

        return false;
    }

    public boolean helper(char[][] board, String word, int row, int col, int[][] visited){
        if(word.length() == 0){
            return true;
        } else if(row < 0 || col < 0 || row >= board.length || col >= board[0].length){
            return false;
        } else if(visited[row][col] == 1 || word.charAt(0) != board[row][col]){
            return false;
        }

        visited[row][col] = 1;
        word = word.substring(1);
        if(helper(board, word, row + 1, col, visited) || helper(board, word, row - 1, col, visited) ||
            helper(board, word, row, col + 1, visited) || helper(board, word, row, col - 1, visited)){
                return true;
        }
        visited[row][col] = 0;

        return false;
    }
}
