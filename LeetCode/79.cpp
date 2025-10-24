class Solution {
    vector<vector<char>> board;
    string word;
    vector<vector<bool>> visited;
    int dR[4] = {-1, 1, 0, 0};
    int dC[4] = {0, 0, -1, 1};

    bool dfs(int row, int col, int depth){
        if (row < 0 || row >= board.size() || col < 0 || col >= board[0].size() || visited[row][col]){
            return false;
        }

        if (board[row][col] != word[depth]){
            return false;
        }

        if (depth == word.size()-1){
            return true;
        }

        visited[row][col] = true;

        for (int i = 0; i < 4; i++){
            if (dfs(row+dR[i], col+dC[i], depth+1)){
                return true;
            }
        }

        visited[row][col] = false;

        return false;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        this->board = board;
        this->word = word;

        for (int i = 0; i <board.size(); i++){
            for (int j = 0; j < board[0].size(); j++){
                if (board[i][j] == word[0]){
                    // cout << format("start on {} {}", i, j) << endl; 
                    visited = vector<vector<bool>>(board.size(), vector<bool>(board[0].size(), false));
                    if (dfs(i, j, 0)){
                        return true;
                    }
                }
                
            }
        }

        return false;
    }
};
