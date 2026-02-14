class Solution {
    int dSum(int num){
        int sum = 0;
        while (num >= 10){
            sum += num % 10;
            num /= 10;
        }
        sum += num;
        return sum;
    }
public:
    int differenceOfSum(vector<int>& nums) {
        int elementSum = 0;
        int digitSum = 0;
        for (int num : nums){
            elementSum += num;
            digitSum += dSum(num);
        }

        return abs(elementSum - digitSum);
    }
};
