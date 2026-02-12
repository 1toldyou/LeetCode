class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int m = triangle.size();
        int n = triangle[m-1].size();
        
        vector dp(m, vector(n, INT_MAX));
        dp[0][0] = triangle[0][0];

        for (int i = 0; i < m-1; i++){
            for (int j = 0; j <= i; j++){
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+triangle[i+1][j]);
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+triangle[i+1][j+1]);
            }
        }

        int smallest = INT_MAX;
        for (int num : dp[m-1]){
            smallest = min(smallest, num);
        }

        return smallest;
    }
};
