class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        if (n <= 1){
            return n;
        }
        
        int a = 0;
        int b = 0;
        int maxSize = 0;
        map<char, int> view;
        view[s[0]] = 0;

        while (b < n-1){
            b++;
            auto newChar = s[b];
            if (view.count(newChar) > 0){
                for (int i = a; i < view[newChar]; i++){
                    view.erase(s[i]);
                }

                a = view[newChar] + 1;
            }

            view[newChar] = b;
            maxSize = max(maxSize, b - a + 1);
        }

        return maxSize;
    }
};
