class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int cols = matrix[0].size();
        int rows = matrix.size();
        vector<int> result;
        
        int x = 0;
        int y = 0;
        int state = 0; // go right, down, left, up

        int left = 0;
        int right = cols - 1;
        int up = 1;
        int down = rows - 1;
        // cout << format("right={} down={}\n", right, down);

        for (int i = 0; i < cols*rows; i++){
            // cout << format("x={} y={}\n", x, y);
            result.emplace_back(matrix[y][x]);
            switch(state){
                case 0:
                    if (x == right){
                        // cout << "reaching right border\n";
                        state = 1;
                        y++;
                        right--;
                    }
                    else {
                        x++;
                    }
                    break;
                case 1:
                    if (y == down){
                        // cout << "reaching down border\n";
                        state = 2;
                        x--;
                        down--;
                    }
                    else {
                        y++;
                    }
                    break;
                case 2:
                    if (x == left){
                        // cout << "reaching left border\n";
                        state = 3;
                        y--;
                        left++;
                    }
                    else {
                        x--;
                    }
                    break;
                case 3:
                    if (y == up){
                        // cout << "reaching up border\n";
                        state = 0;
                        x++;
                        up++;
                    }
                    else {
                        y--;
                    }
                    break;
            }
        }


        return result;
    }
};
