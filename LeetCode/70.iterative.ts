function climbStairs(n: number): number {
    let steps = new Array(n);
    steps[0] = 1;
    steps[1] = 2;
    for (let i = 2; i < n; i++){
        steps[i] = steps[i-1] + steps[i-2];
    }

    return steps[n-1];
};
