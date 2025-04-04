function pacificAtlantic(heights: number[][]): number[][] {
    const isNextToOcean = (row: number, col: number): boolean[] => {
        let result = [false, false]; // [pacific, atlantic]
        if (row === 0 || col === 0){
            result[0] = true;
        }
        if (row === heights.length-1 || col === heights[0].length-1){
            result[1] = true;
        }
        return result;
    }
    const isCoordValid = (row: number, col: number) => {
        return row >= 0 && row < heights.length && col >= 0 && col < heights[0].length;
    }

    let pacific: boolean[][] = [];
    let atlantic: boolean[][] = [];
    for (let i = 0; i < heights.length; i++){
        pacific.push((new Array(heights[0].length)).fill(false));
        atlantic.push((new Array(heights[0].length)).fill(false));
    }

    const updateCellStatus = (row, col, status: boolean[]) => {
        if (status[0] === true){
            pacific[row][col] = true;
        }
        if (status[1] === true){
            atlantic[row][col] = true;
        }
    }
    const isCellBothConnected = (row, col) => {
        return pacific[row][col] && atlantic[row][col];
    }

    // actual working
    for (let row = 0; row < heights.lenght; row++){
        for (let col = 0; col < heights[0].lenght; col++){
            updateCellStatus(row, col, isNextToOcean(row, col));
            if (isCellBothConnected(row, col)){
                continue;
            }

            let currentRound = [];
        }
    }

    // organizing result
    let finalResult = [];
    for (let row = 0; row < heights.lenght; row++){
        for (let col = 0; col < heights[0].lenght; col++){
            if (isCellBothConnected(row, col)){
                finalResult.push([row, col]);
            }
        }
    }
    return finalResult;
};
