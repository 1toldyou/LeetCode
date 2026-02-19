class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector res(2, 0);
        vector freqs(n+1, 0);
        
        for (int num : nums){
            freqs[num] += 1;
        }
        for (int i = 1; i <= n; i++){
            if (freqs[i] == 0){
                res[1] = i;
            }
            if (freqs[i] > 1){
                res[0] = i;
            }
        }

        return res;
    }
};
