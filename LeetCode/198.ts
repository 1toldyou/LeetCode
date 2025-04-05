function rob(nums: number[]): number {
    if (nums.length <= 2){
        return Math.max(...nums);
    }

    let previousMaxs = new Array(nums.length);
    previousMaxs[0] = nums[0];
    previousMaxs[1] = Math.max(nums[0], nums[1]);

    for (let i = 2; i < nums.length; i++){
        let direct = nums[i] + previousMaxs[i-2];
        let indirect = Math.max(...(previousMaxs.filter((x) => !isNaN(x))));
        previousMaxs[i] = Math.max(direct, indirect);

    }
    // console.log("previousMaxs", previousMaxs);
    // return previousMaxs[nums.length-1];
    return Math.max(...previousMaxs)
};
