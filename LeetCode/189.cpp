class Solution {
    void work(vector<int>& nums){
        
    }
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;

        vector<int> og(nums);
        for (int i = 0; i < k; i++){
            nums[i] = og[i+n-k];
        }
        for (int i = k; i < n; i++){
            nums[i] = og[i-k];
        }
    }
};
