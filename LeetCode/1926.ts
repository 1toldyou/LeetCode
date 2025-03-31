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
        return coord.x === 0 || coord.x === maze.length-1 || coord.y === 0 || coord.y === maze[0].length-1;
    };

    let visited: boolean[][] = [];
    for (let i = 0; i < maze.length; i++){
        visited.push((new Array(maze[i].length)).fill(false));
    };
    visited[entrance[0]][entrance[1]] = true;

    let currentLevel = [toCoord(entrance)];
    let steps = 1;
    while (currentLevel.length > 0){ // otherwise options are exhuasted
        let nextLevel = [];
        for (let coord of currentLevel){
            for (let next of [{x: coord.x, y: coord.y+1}, {x: coord.x, y: coord.y-1}, {x: coord.x+1, y: coord.y}, {x: coord.x-1, y: coord.y}]){
                if (!canGo(next)){ // will check if it out of bounds
                    continue;
                }

                if (visited[next.x][next.y] === true){
                    continue;
                }

                if (isExit(next)){
                    return steps;
                }
                nextLevel.push(next);
                visited[next.x][next.y] = true;
            }
        }
        currentLevel = nextLevel;
        steps++;
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