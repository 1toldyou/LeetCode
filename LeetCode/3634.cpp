class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int a = 0;
        int b = n - 1;
        int count = 0;

        while(a < b){
            // cout << format("a={} b={} nums[a]={} nums[b]={}\n", a, b, nums[a], nums[b]);
            if (nums[a] * k >= nums[b]){  // 
                break;
            }
            if (b - a == 1){  // n = 2
                count++;
                break;
            }

            float moveA = nums[b] * 1.0 / nums[a+1] * 1.0;
            float moveB = nums[b-1] * 1.0 / nums[a] * 1.0;
            cout << format("curr={} moveA={} moveB={}\n", nums[b]/nums[a], moveA, moveB);
            if (moveA <= moveB){
                cout << format("removing {}\n", nums[a]);
                a++;
            }
            else {
                cout << format("removing {}\n", nums[b]);
                b--;
            }
            count++;
        }
        
        return count;
    }
};
