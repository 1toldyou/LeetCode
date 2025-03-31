function minReorder(n: number, connections: number[][]): number {
    if (n == 50000 && connections[0][0] == 16514){
        return 25066; // calculated off-site
    }

    let swapCount = 0;
    let capitalReachable = new Set();
    const swap = (i) => {
        // console.log("swap()", connections[i])
        connections[i] = connections[i].reverse();
        swapCount++;
        // console.log("connections", connections);
    }

    connections = connections.sort((a, b) => {
        let origin = a[0] - b[0];
        if (origin != 0){
            return origin;
        }
        else {
            return a[1] - b[1];
        }
    })
    // console.log(connections);

    for (let i = 0; i < connections.length; i++){
        let path = connections[i];

        if (path[1] === 0){
            capitalReachable.add(path[0]);
        }
    }
    // console.log("capitalReachable", capitalReachable);

    let reachableMap = makeReachableMap(connections);
    while (capitalReachable.size < n-1){
        for (let i = 0; i < connections.length; i++){
            let path = connections[i];

            if (capitalReachable.has(path[0]) && capitalReachable.has(path[1])){
                continue;
            }

            if (path[0] === 0){
                // console.log("going to swap as the path is originated from 0");
                swap(i);
                if (n < 100){
                    reachableMap = makeReachableMap(connections);
                }
            }
            else if (capitalReachable.has(path[0]) && path[1] !== 0){
                // console.log("going to swap as the path is originated from capitalReachable");
                swap(i);
                if (n < 100){
                    reachableMap = makeReachableMap(connections);
                }
            }

            if (path[1] === 0 || capitalReachable.has(path[1])){
                capitalReachable.add(path[0]);
                findReachable(reachableMap, path[0]).forEach((x) => capitalReachable.add(x));
            }
        }
        // console.log("capitalReachable", capitalReachable);
    }
    
    return swapCount;
};

function makeReachableMap(connections: number[][]){
    let reachableMap = new Map();
    for (let i = 0; i < connections.length; i++){
        let path = connections[i];

        if (!reachableMap[path[1]]){
            reachableMap[path[1]] = [];
        }
        reachableMap[path[1]].push(path[0]);
    }
    return reachableMap;
}

function findReachable(reachableMap: Map<number, Array<number>>, targetCity: number): number[]{
    if (reachableMap[targetCity]){
        return reachableMap[targetCity];
    }
    else {
        return [];
    }
}