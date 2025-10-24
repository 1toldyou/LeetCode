typedef long long LL;

class Solution {
    vector<int> piles;
    int h;

    bool isPossible(int k){
        LL accu = 0;
        for (LL x : piles){
            accu += (x / k) + (x % k > 0);
        }
        return accu <= h;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        this->piles = piles;
        this->h = h;

        int low = 0;
        int high = 0;
        for (int x : piles){
            high = max(high, x);
        }

        while (low+1 < high){
            int mid = low + (high - low)/2;
            if (isPossible(mid)){
                high = mid;
            } 
            else {
                low = mid;
            }
        }
        return high;
    }


};
