class Solution {
    vector<int> cache;

    int _fib(int n){
        if (n <= 1){
            return n;
        }
        
        if (cache[n] > -1){
            return cache[n];
        }

        return cache[n] = _fib(n-1) + _fib(n-2);
    }
public:
    int fib(int n) {
        cache = vector<int>(n+1, -1);
        return _fib(n);
    }
};
