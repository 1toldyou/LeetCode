function countPairs(nums: number[], k: number): number {
    let map = new Map();
    for (let i = 0; i < nums.length; i++){
        if (!map[nums[i]]){
            map[nums[i]] = [];
        }
        map[nums[i]].push(i);
    }
    // console.log(map);
    let validPairCount = 0;
    for (let vals of Object.values(map)){
        if (vals.length < 2){
            continue;
        }
        for (let i = 0; i < vals.length-1; i++){
            for (let j = i+1; j < vals.length; j++){
                if ((vals[i] * vals[j]) % k === 0){
                    validPairCount++;
                }
            }
        }
    }
    return validPairCount;
};
