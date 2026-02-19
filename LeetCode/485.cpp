class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        int count = 0;
        for (int i = 0; i < n; i++){
            switch(nums[i]){
                case 0:
                    count = 0;
                    break;
                case 1:
                    count++;
                    ans = max(ans, count);
                    break;
            }
        }
        return ans;
    }
};
