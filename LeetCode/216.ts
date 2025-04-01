function combinationSum3(k: number, n: number): number[][] {
    if (n < k){
        return [];
    }

    const isComboValid = (arr: number[]) => {
        let sum = arr.reduce((accu, curr) => accu + curr);
        if (sum < n){
            return -1;
        }
        else if (sum > n){
            return 1;
        }
        else {
            return 0;
        }
    }

    let combos = [[]]; 
    for (let generation = 0; generation < k; generation++){
        let newCombos = [];
        for (let currentCombo of combos){
            let newDigits = getAvailableDigits(currentCombo);
            // console.log("currentCombo", currentCombo, "newDigits", newDigits);
            for (let newDigit of newDigits){
                let newCombo = [...currentCombo, newDigit];
                let check = isComboValid(newCombo);
                if ((generation < k-1 && check < 0) || (generation == k-1 && check === 0)){
                    newCombos.push(newCombo);
                }
            }
        }
        // console.log("newCombos", newCombos);
        combos = newCombos;
    }
    return combos;
}

// let allDigits = new Set([1,2,3,4,5,6,7,8,9]);
function getAvailableDigits(arr: number[]): number[] {
    // return Array.from(allDigits.difference(new Set(arr)));  // too new
    // return [1,2,3,4,5,6,7,8,9].filter((x) => !arr.includes(x));
    if (arr.length === 0){
        return [1,2,3,4,5,6,7,8,9];
    }

    let result = [];
    for (let num = arr[arr.length-1]+1; num <= 9; num++){
        result.push(num);
    }
    return result;
}
