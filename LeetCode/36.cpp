class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++){
            int existR[10] = {}; 
            int existC[10] = {}; 
            for (int j = 0; j < 9; j++){
                if (board[i][j] != '.'){
                    int num = board[i][j] - '0';
                    if (existR[num]){
                        return false;
                    }
                    existR[num] = true;
                }
                if (board[j][i] != '.'){
                    int num = board[j][i] - '0';
                    if (existC[num]){
                        return false;
                    }
                    existC[num] = true;
                }
            }
        }

        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                int exist[10] = {}; 
                for (int u = 0; u < 3; u++){
                    for (int v = 0; v < 3; v++){
                        if (board[i*3+u][j*3+v] != '.'){
                            int num = board[i*3+u][j*3+v] - '0';
                            if (exist[num]){
                                return false;
                            }
                            exist[num] = true;
                        }
                    }
                }
            }
        }

        return true;
    }
};
