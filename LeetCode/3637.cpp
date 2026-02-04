class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        int state = 1;
        for (int i = 1; i < n; i++){
            // cout << format("{} state={}", nums[i], state) << endl;
            if (nums[i] == nums[i-1]){
                return false;
            }
            switch(state){
                case 1:
                    if (nums[i] > nums[i-1]){

                    }
                    else {
                        if (i == 1){
                            return false;
                        }
                        state = 2;
                    }
                    break;
                case 2:
                    if (nums[i] < nums[i-1]){

                    }
                    else {
                        state = 3;
                    }
                    break;
                case 3:
                    if (nums[i] > nums[i-1]){

                    }
                    else {
                        return false;
                    }
                    break;
            }
        }

        return state == 3;
    }
};
