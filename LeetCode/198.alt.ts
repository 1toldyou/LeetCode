function rob(nums: number[]): number {
    if (nums.length <= 2){
        return Math.max(...nums);
    }

    let previousMaxs = new Array(nums.length);
    previousMaxs[0] = nums[0];
    previousMaxs[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < nums.length; i++){
        previousMaxs[i] = Math.max(nums[i] + previousMaxs[i-2], previousMaxs[i-1]);
    }
    // console.log("previousMaxs", previousMaxs);
    // return previousMaxs[nums.length-1];
    // return Math.max(...previousMaxs);
    return Math.max(previousMaxs[nums.length-1], previousMaxs[nums.length-2])
};
