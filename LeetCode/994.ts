function orangesRotting(grid: number[][]): number {
    const hasFresh = () => {
        for (let i = 0; i < grid.length; i++){
            for (let j = 0; j < grid[0].length; j++){
                if (grid[i][j] === 1){
                    return true;
                }
            }
        }
        return false;
    };
    const isFreshOrange = (row, col) => {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length){
            return false;
        }

        return grid[row][col] === 1;
    };

    let currentCycle = [];
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[0].length; j++){
            if (grid[i][j] === 2){
                currentCycle.push([i, j]);
            }
        }
    }

    let steps = 0;
    while (currentCycle.length > 0){
        steps++;
        let nextCycle = [];
        for (let [row, col] of currentCycle){
            for (let [nextRow, nextCol] of [[row, col-1], [row, col+1], [row+1, col], [row-1, col]]){
                if (!isFreshOrange(nextRow, nextCol)){
                    continue;
                }

                grid[nextRow][nextCol] = 2;
                nextCycle.push([nextRow, nextCol]);
            }
        }
        currentCycle = nextCycle;
        // console.log("grid", grid);
        // console.log("nextCycle", nextCycle);
    }

    if (hasFresh()){
        return -1;
    }
    else {
        return Math.max(steps-1, 0);
    }
};