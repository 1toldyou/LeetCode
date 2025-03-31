function findCircleNum(isConnected: number[][]): number {
    let n = isConnected.length;
    if (n == 1){
        return 1;
    }

    let connected = new Map();
    for (let i = 0; i < n; i++){
        connected[i] = new Set();
        for (let j = 0; j < n; j++){
            if (isConnected[i][j] == 1){
                dig(isConnected, connected, i, j);
            }
        }
    }

    // console.log("connected", connected);

    // let provinceCount = 0;
    // while (connected.size > 0){
    //     let key = connected.keys()[0];


    // }

    let unique = new Set();
    for (let value of Object.values(connected)){
        // console.log("value", value);
        // let hash = Array.from(value).sort().join("");
        // console.log(hash);
        // unique.add(hash);
        // unique.add(Array.from(value).sort().join(""));
        unique.add(Array.from(value).sort().join(""));
    }
    // console.log("unique", unique);

    return unique.size;
};

function dig(all: number[][], connected: Map<number, Set<number>>, masterCity: number, currentCity: number){
    if (connected[masterCity].has(currentCity)){
        return;
    }

    connected[masterCity].add(currentCity);

    for (let j = 0; j < all.length; j++){
        if (all[currentCity][j] == 1){
            dig(all, connected, masterCity, j);
        }
    }
}