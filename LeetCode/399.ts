function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    let map = new Map();
    for (let i = 0; i < equations.length; i++){
        // forward
        if (!map[equations[i][0]]){
            map[equations[i][0]] = new Map();
        }
        map[equations[i][0]][equations[i][1]] = values[i];

        // reverse
        if (!map[equations[i][1]]){
            map[equations[i][1]] = new Map();
        }
        map[equations[i][1]][equations[i][0]] = 1 / values[i];
    }
    // console.log(map);

    let results = [];
    for (let query of queries){
        if (!map[query[0]] || !map[query[1]]){
            results.push(-1);
            continue;
        }
        if (query[0] === query[1]){
            results.push(1);
            continue;
        }

        let path = findPath(map, query[0], query[1], []);
        // console.log("path", query, path);

        if (path.length < 2){
            results.push(-1);
            continue;
        }

        let val = map[path[0]][path[1]];
        for (let i = 2; i < path.length; i++){
            val *= map[path[i-1]][path[i]];
        }
        results.push(val);
    }

    return results;
};

function findPath(map, from, to, visited: string[]): string[]{
    // console.log("findPath()", from, to, visited);
    if (!map[from] || !map[to] || from === to){
        return [];
    }

    if (map[from][to]){
        return [from, to];
    }

    let routes = [];
    // console.log(`findPath() map[${from}]:`, map[from]);
    for (let option of Object.keys(map[from])){
        if (!visited.includes(option)){
            routes.push(findPath(map, option, to, [...visited, from]));
        }
    }

    // console.log("findPath() routes:", routes);
    routes = routes.filter((ele) => ele.length > 0);
    if (routes.length == 0){
        return [];
    }
    return [from, ...routes.sort((a, b) => a.length - a.length)[0]];
}