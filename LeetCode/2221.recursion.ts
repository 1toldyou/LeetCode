function triangularSum(nums: number[]): number {
    if (nums.length == 1){
        return nums[0];
    }

    let next = new Array(nums.length-1).fill(0);
    for (let i = 0; i < nums.length; i++){
        if (i < nums.length - 1){
            next[i] += nums[i];
        }
        if (i > 0){
            next[i-1] += nums[i];
        }
    }
    for (let i = 0; i < next.length; i++){
        next[i] = next[i] % 10;
    }
    // console.log(next);
    return triangularSum(next);
};
