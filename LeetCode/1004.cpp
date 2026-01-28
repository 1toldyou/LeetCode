class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
        int left = -1;
        int right = -1;
        int ones = 0;
        int zeros = 0;
        int maxLength = 0;
        while (right < n-1){
            if (nums[++right] == 1){
                ones++;
            }
            else {
                zeros++;
            }

            while (zeros > k){
                if (nums[++left] == 1){
                    ones--;
                }
                else {
                    zeros--;
                }
            }

            maxLength = max(maxLength, right - left);
        }

        return maxLength;
    }
};
