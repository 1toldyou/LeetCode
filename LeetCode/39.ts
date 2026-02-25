function combinationSum(candidates: number[], target: number): number[][] {
    let unique = {};

    const bt = (nums: number[], sum: number) => {
        if (sum > target){
            return;
        }
        if (sum == target){
            unique[nums.sort().join(",")] = true;
            return;
        }
        for (let num of candidates){
            bt([...nums, num], sum + num);
        }
    }

    bt([], 0);

    return Array.from(Object.keys(unique)).map(k => k.split(",").map(Number))
};
