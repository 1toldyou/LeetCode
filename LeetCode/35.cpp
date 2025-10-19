class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        if (target <= nums[0]){
            return 0;
        }
        if (target > nums[n-1]){
            return n;
        }
        if (target == nums[n-1]){
            return n-1;
        }

        int low = -1;
        int high = n-1;
        while (low+1 < high){
            int mid = low + (high-low)/2;
            // cout << format("low={} high={} mid={}", low, high, mid) << endl;
            if (nums[mid] == target){
                return mid;
            }
            if (nums[mid] < target && nums[mid+1] > target){
                return mid+1;
            }
            if (nums[mid] < target){
                low = mid;
            }
            else {
                high = mid;
            }
        }
        return high;
    }
};
