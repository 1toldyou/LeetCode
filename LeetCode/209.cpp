class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        vector<int> prefixSum(n);
        prefixSum[0] = nums[0];
        for (int i = 1; i < n; i++){
            prefixSum[i] = nums[i] + prefixSum[i-1];
        }

        if (prefixSum[n-1] < target){
            return 0;
        }
        if (prefixSum[n-1] == target){
            return n;
        }

        auto isWindowPossible = [&](int windowSize){
            for (int i = windowSize-1; i < n; i++){
                if ((prefixSum[i] - (i-windowSize>=0 ? prefixSum[i-windowSize] : 0)) >= target){
                    return true;
                }
            }
            return false;
        };

        int low = 0;
        int high = nums.size();
        while (low+1 < high){
            int mid = low + (high-low)/2;
            // cout << format("mid={}", mid) << endl;

            if (isWindowPossible(mid)){
                high = mid;
            }
            else {
                low = mid;
            }
        }

        return high;
    }
};
