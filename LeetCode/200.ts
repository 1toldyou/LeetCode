function numIslands(grid: string[][]): number {
    const isCoordValid = (row, col) => {
        return row >= 0 && row < grid.length && col >= 0 && col < grid[0].length;
    };
    let everVisited = make2DArray(grid.length, grid[0].length);
    let islandCount = 0;
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[0].length; j++){
            if (grid[i][j] === "1"){
                if (everVisited[i][j] === false){
                    // console.log("new island at", i, j);
                    let currentIsland = make2DArray(grid.length, grid[0].length);
                    currentIsland[i][j] = true;
                    everVisited[i][j] = true;

                    let currentBatch = [[i, j]];
                    while (currentBatch.length > 0){
                        // console.log("currentBatch", currentBatch);
                        let nextBatch = [];
                        for (let coord of currentBatch){
                            for (let nextCoord of [
                                [coord[0]+1, coord[1]],
                                [coord[0]-1, coord[1]],
                                [coord[0], coord[1]+1],
                                [coord[0], coord[1]-1],
                            ]){
                                if (!isCoordValid(nextCoord[0], nextCoord[1])){
                                    continue;
                                }

                                if (currentIsland[nextCoord[0]][nextCoord[1]]){
                                    continue;
                                }

                                if (grid[nextCoord[0]][nextCoord[1]] === "0"){
                                    continue;
                                }

                                nextBatch.push(nextCoord);
                                currentIsland[nextCoord[0]][nextCoord[1]] = true;
                                everVisited[nextCoord[0]][nextCoord[1]] = true;
                            }
                        }
                        currentBatch = nextBatch;
                    }
                    islandCount++;
                }
            }
        }
    }
    return islandCount;
};

function make2DArray(row, col): boolean[][]{
    let result = new Array(row);
    for (let i = 0; i < row; i++){
        result[i] = (new Array(col)).fill(false);
    }
    return result;
}
