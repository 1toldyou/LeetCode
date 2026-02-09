class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int a = 0;
        int b = n - 1;
        int count = 0;

        while(a < b){
            cout << format("a={} b={}\n", a, b);
            if (nums[a] * k >= nums[b]){  // 
                break;
            }
            if (b - a == 1){  // n = 2
                count++;
                break;
            }

            if (nums[b] / nums[a+1] >= nums[b-1] / nums[a]){
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
