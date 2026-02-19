class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int n = nums.size();
        vector ans(n, 0);
        vector freqs(101, 0);

        for (int num : nums){
            freqs[num]++;
        }

        for (int i = 0; i < n; i++){
            for (int j = 0; j < nums[i]; j++){
                ans[i] += freqs[j];
            }
        }

        return ans;
    }
};
