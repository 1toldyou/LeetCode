class Solution {
public:
    string reorganizeString(string s) {
        if (s.size() == 1){
            return s;
        }

        typedef pair<int, char> PR;

        map<char, int> initFreqs;
        for (char c : s){
            if (!initFreqs.count(c)){
                initFreqs[c] = 0;
            }
            initFreqs[c] += 1;
        }

        priority_queue<PR> freqs;
        for (auto [key, val] : initFreqs){
            freqs.push(make_pair(val, key));
        }

        string ret;
        while (freqs.size() >= 2){
            PR most1 = freqs.top();
            freqs.pop();
            PR most2 = freqs.top();
            freqs.pop();
            // cout << format("most1={},{} most2={},{} freqs={}", most1.first, most1.second, most2.first, most2.second, freqs.size()) << endl;
            ret += most1.second;
            ret += most2.second;
            
            most1.first--;
            most2.first--;
            if (most1.first > 0){
                freqs.push(most1);
            }
            if (most2.first > 0){
                freqs.push(most2);
            }
        }
        if (freqs.size() == 0){
            return ret;
        }

        if (freqs.top().first == 1){
            return ret + freqs.top().second;
        }
        else {
            return "";
        }
    }
};
