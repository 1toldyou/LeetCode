class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int, int> occurrences;
        for (auto a: arr){
            if (!occurrences.count(a)){
                occurrences[a] = 0;
            }
            occurrences[a]++;
        }

        set<int> counts;
        for (auto const& x : occurrences){
            if (counts.count(x.second)){
                return false;
            }
            counts.insert(x.second);
        }

        return true;
    }
};
