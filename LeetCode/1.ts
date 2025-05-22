function twoSum(nums: number[], target: number): number[] {
    // // the efficient way
    // let pos = [];
    // let neg = [];
    // for (let i = 0; i < nums.length; i++){
    //     if (nums[i] >= 0){
    //         pos[nums[i]] = i;
    //     }
    //     else {
    //         neg[Math.abs(nums[i])] = i;
    //     }
    // }
    // for (let i = 0; i < nums.length; i++){
    //     let num = nums[i];
    //     let diff = target - num;
    //     if (diff > 0){
    //         if (pos[diff] != undefined){
    //             if (i != pos[diff]){
    //                 return [i, pos[diff]];
    //             }
    //         }
    //     }
    //     else {
    //         if (neg[diff] != undefined){
    //             if (i != neg[diff]){
    //                 return [i, neg[diff]];
    //             }
    //         }
    //     }
    // }

    // let map = new Map();
    // for (let i = 0; i < nums.length; i++){
    //     if (map[nums[i]]){
    //         map[nums[i]].push(i);
    //     }
    //     else {
    //         map[nums[i]] = [i];
    //     }
    // }
    // for (let i = 0; i < nums.length; i++){
    //     let num = nums[i];
    //     let diff = target - num;
    //     if (map[diff]){
    //         if (map[diff].length >= 2){
    //             return [map[diff][0], map[diff][1]];
    //         }
    //         else {
    //             if (i != map[diff][0]){
    //                 return [i, map[diff][0]];
    //             }
    //         }
    //     }
    // }

    let pos2 = [];
    let neg2 = [];
    const getVal = (key) => {
        if (key < 0){
            return neg2[Math.abs(key)];
        }
        else {
            return pos2[key];
        }
    };
    const setVal = (key, val) => {
        if (key < 0){
            neg2[Math.abs(key)] = val;
        }
        else {
            pos2[key] = val;
        }
    };

    for (let i = 0; i < nums.length; i++){
        if (getVal(nums[i])){
            getVal(nums[i]).push(i);
        }
        else {
            setVal(nums[i], [i]);
        }
    }
    for (let i = 0; i < nums.length; i++){
        let num = nums[i];
        let diff = target - num;
        if (getVal(diff)){
            if (getVal(diff).length >= 2){
                return [getVal(diff)[0], getVal(diff)[1]];
            }
            else {
                if (i != getVal(diff)[0]){
                    return [i, getVal(diff)[0]];
                }
            }
        }
    }

};
