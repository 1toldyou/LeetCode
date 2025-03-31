let globalBest = Number.MAX_SAFE_INTEGER; // need reset on every run;

function nearestExit(maze: string[][], entrance: number[]): number {
    globalBest = Number.MAX_SAFE_INTEGER;
    let coord: Coord = {x: entrance[0], y: entrance[1]};

    // let depth = Number.MAX_SAFE_INTEGER;
    let options = [
        findPath(maze, {x: coord.x, y: coord.y+1}, [coord], 0),
        findPath(maze, {x: coord.x, y: coord.y-1}, [coord], 0),
        findPath(maze, {x: coord.x+1, y: coord.y}, [coord], 0),
        findPath(maze, {x: coord.x-1, y: coord.y}, [coord], 0),
    ].filter((x) => x > 0);

    if (options.length === 0){
        return -1;
    }
    return Math.min(...options);
};

type Coord = {
    x: number
    y: number
}



function isExit(maze: string[][], coord: Coord){
    if (!canGo(maze, coord)){
        // console.log(coord, "cannot be exit as it cannot be reached");
        return false;
    }

    return coord.x === 0 || coord.x === maze.length-1 || coord.y === 0 || coord.y === maze[0].length-1;
}

function isWall(maze: string[][], coord: Coord): boolean {
    try {
        return maze[coord.x][coord.y] === "+";
    } catch (e) {
        console.log("isWall() bad coordinate", coord)
        return false;
    }
}

function canGo(maze: string[][], coord: Coord){
    return !(coord.x < 0 || coord.x >= maze.length || coord.y < 0 || coord.y >= maze[0].length || isWall(maze, coord));
}

function findPath(maze: string[][], coord: Coord, previousPath: Coord[], depth: number): number {
    depth++;
    if (depth > globalBest){
        console.log(`better solution ${globalBest} already exist`);
        return -1;
    }

    // console.log("findPath()", coord);
    if (!canGo(maze, coord)){
        // console.log("findPath() cannot go", coord);
        return -1;
    }
    if (isExit(maze, coord)){
        globalBest = Math.min(globalBest, depth);
        console.log("findPath()", coord, "is exit", `globalBest=${globalBest}`);
        return 1;
    }

    // let up = ;
    // let down = ;
    // let left = ;
    // let right = ;

    let validDirections = [
        {x: coord.x, y: coord.y+1}, 
        {x: coord.x, y: coord.y-1},
        {x: coord.x+1, y: coord.y},
        {x: coord.x-1, y: coord.y},
    ].filter((next) => !beenTo(next, previousPath));
    // console.log("findPath()", coord, "validDirections", validDirections);

    for (let next of validDirections){
        if (isExit(maze, next)){
            return 2;
        }
    }

    let outcomes = [];
    for (let next of validDirections){
        outcomes.push(findPath(maze, next, [...previousPath, coord], depth));
    }
    // console.log("outcomes", outcomes);
    outcomes = outcomes.filter((x) => x >= 0);
    if (outcomes.length === 0){
        return -1
    }
    return 1 + Math.min(...outcomes);
}

function beenTo(coord: Coord, previousPath: Coord[]): boolean {
    for (let previousCoord of previousPath){
        if (objectsAreEqual(coord, previousCoord)){
            return true;
        }
    }
    return false;
}

function arraysAreEqual(arr1, arr2) {
    return JSON.stringify(arr1) === JSON.stringify(arr2);
}

function objectsAreEqual(obj1, obj2) {
    // If they are not the same type, they are not equal
    if (typeof obj1 !== 'object' || typeof obj2 !== 'object' || obj1 === null || obj2 === null) {
        return false;
    }

    // Compare the number of keys in both objects
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);
    if (keys1.length !== keys2.length) {
        return false;
    }

    // Compare the values for each key
    for (let key of keys1) {
        if (obj1[key] !== obj2[key]) {
            return false;
        }
    }

    return true;
}