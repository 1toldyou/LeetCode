class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = -1;
        int high = nums.size() - 1;
        while (low+1 < high){
            int mid = low + (high-low)/2;
            // cout << format("low={} high={} mid={}", low, high, mid) << endl;
            if (nums[mid] == target){
                return mid;
            }
            else if (nums[mid] < target){
                low = mid;
            }
            else {
                high = mid;
            }
        }

        if (nums[high] == target){
            return high;
        }
        return -1;
    }
};
