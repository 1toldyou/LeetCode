class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        set<int> unique;
        for (int num : nums){
            if (num > 0){
                unique.insert(num);
            }
        }

        return unique.size();
    }
};
