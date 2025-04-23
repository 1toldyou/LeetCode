function countLargestGroup(n: number): number {
    const digitSum = (num: number) => {
        let s = num.toString();
        let sum = 0;
        for (let c of s){
            sum += parseInt(c);
        }
        return sum;
    }

    let map = new Map();
    for (let i = 1; i <= n; i++){
        let ds = digitSum(i);
        if (!map[ds]){
            map[ds] = [];
        }
        map[ds].push(i);
    }
    // console.log(map);

    let biggestGroupSize = 0;
    for (let x of Object.values(map)){
        biggestGroupSize = Math.max(biggestGroupSize, x.length);
    }
    // console.log("biggestGroupSize", biggestGroupSize)

    let biggestGroupCount = 0;
    for (let x of Object.values(map)){
        if (x.length === biggestGroupSize){
            biggestGroupCount++;
        }
    }

    return biggestGroupCount;
};
