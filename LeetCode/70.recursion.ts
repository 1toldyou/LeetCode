let cache = new Map();

function climbStairs(n: number): number {
    if (n == 1){
        return 1;
    }
    if (n == 2){
        return 2;
    }

    if (cache[n]){
        return cache[n];
    }

    let result = climbStairs(n-1) + climbStairs(n-2);
    cache[n] = result;
    return result;
};
