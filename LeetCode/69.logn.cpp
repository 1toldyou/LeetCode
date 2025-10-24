class Solution {
public:
    int mySqrt(int x) {
        if (x <= 1){
            return x;
        }

        int low = 0;
        int high = x;
        while (low+1 < high){
            long long mid = low + (high-low)/2;
            long long pow = mid*mid;
            if (pow == x){
                return mid;
            }
            if (pow < x){
                low = mid;
            }
            else {
                high = mid;
            }
        }
        return high-1;
    }
};
