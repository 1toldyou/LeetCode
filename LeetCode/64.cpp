class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid[0].size();
        int m = grid.size();
        vector dp(m, vector<int>(n, INT_MAX));

        dp[0][0] = grid[0][0];

        for (int row = 0; row < m; row++){
            for (int col = 0; col < n; col++){
                if (row > 0){
                    dp[row][col] = min(dp[row][col], dp[row-1][col]);
                }
                if (col > 0){
                    dp[row][col] = min(dp[row][col], dp[row][col-1]);
                }

                if (row == 0 && col == 0){
                    continue;
                }
                dp[row][col] += grid[row][col];
            }
        }

        return dp[m-1][n-1];
    }
};
