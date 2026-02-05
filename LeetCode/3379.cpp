class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n); 
        for (int i = 0; i < n; i++){
            int num = nums[i];
            int pos = i;
            if (num > 0){
                pos = (i + num);
            }
            else if (num < 0){
                num %= -n;
                pos = i + num;
                if (pos < 0){
                    pos = n + pos;
                }
            }
            result[i] = nums[pos % n];
        }

        return result;
    }
};
