class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());

        int n = arr.size();
        int minDiff = abs(arr[n-1] - arr[0]);
        for (int i = 0; i < n-1; i++){
            minDiff = min(minDiff, abs(arr[i+1] - arr[i])); 
        }

        vector<vector<int>> res;
        for (int i = 0; i < n-1; i++){
            if (abs(arr[i+1] - arr[i]) == minDiff){
                vector<int> pair = {arr[i], arr[i+1]};
                res.emplace_back(move(pair));
            }
        }

        return res;
    }
};
