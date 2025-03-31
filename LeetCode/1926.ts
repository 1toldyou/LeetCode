function nearestExit(maze: string[][], entrance: number[]): number {
    const isWall = (coord) => {
        try {
            return maze[coord.x][coord.y] === "+";
        } catch (e) {
            return false;
        }
    };
    const canGo = (coord) => {
        return !(coord.x < 0 || coord.x >= maze.length || coord.y < 0 || coord.y >= maze[0].length || isWall(coord));
    };
    const isExit = (coord) => {
        if (!canGo(coord)){
            // console.log(coord, "cannot be exit as it cannot be reached");
            return false;
        }
        return coord.x === 0 || coord.x === maze.length-1 || coord.y === 0 || coord.y === maze[0].length-1;
    };

    let visited: boolean[][] = [];
    for (let i = 0; i < maze.length; i++){
        visited.push((new Array(maze[i].length)).fill(false));
    };
    visited[entrance[0]][entrance[1]] = true;
    let emptyCell = count2D(maze, "."); // including entrance
    let visitedCell = 1;

    let currentLevel = [toCoord(entrance)];
    let steps = 1;
    while (currentLevel.length > 0){
        let nextLevel = [];
        console.log("currentLevel", currentLevel)
        for (let coord of currentLevel){
            let adjacents = [
                {x: coord.x, y: coord.y+1}, 
                {x: coord.x, y: coord.y-1},
                {x: coord.x+1, y: coord.y},
                {x: coord.x-1, y: coord.y},
            ].filter((next) => {
                if (!canGo(next)){ // will check if it out of bounds
                    return false;
                }

                if (visited[next.x][next.y] === true){
                    return false;
                }

                return true;
            });

            for (let next of adjacents){
                if (isExit(next)){
                    return steps;
                }
                nextLevel.push(next);
                visited[next.x][next.y] = true
            }
        }
        currentLevel = nextLevel;
        steps++;
        visitedCell = count2D(visited, true);
    }
    return -1;
};

type Coord = {
    x: number
    y: number
}

function toCoord(arr: number[]): Coord {
    return {
        x: arr[0],
        y: arr[1],
    }
}

function count2D(twoDArr: any[][], target): number{
    return twoDArr.reduce((accu, row) => {
        return accu += row.filter((ele) => ele === target).length;
    }, 0);
}