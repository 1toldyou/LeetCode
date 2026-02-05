/**
 Do not return anything, modify board in-place instead.
 */
function solve(board: string[][]): void {
    const n = board[0].length;
    const m = board.length;

    const dX = [1, -1, 0, 0];
    const dY = [0, 0, 1, -1];

    const makeGrid = () => {
        let grid = new Array(m);
        for (let i = 0; i < m; i++){
            grid[i] = new Array(n).fill(false);
        }
        return grid;
    }

    let bordered = makeGrid();

    const fill = (sR: number, sC: number) => {
        if (board[sR][sC] == "X" || bordered[sR][sC]) return false;

        let current = [[sR, sC]];
        board[sR][sC] = "X";
        while (current.length > 0){
            // console.log("current", current);
            let next = [];
            for (let [r, c] of current){
                // console.log(r, c);
                for (let i = 0; i < 4; i++){
                    let nC = c+dX[i];
                    let nR = r+dY[i];
                    if (nC < 0 || nC == n || nR < 0 || nR == m){
                        continue;
                    }
                    if (board[nR][nC] === "X"){
                        continue;
                    }
                    board[nR][nC] = "X"
                    next.push([nR, nC]);
                }
            }
            current = next;
        }
    };

    const markBordered = (sR: number, sC: number) => {
        if (board[sR][sC] === "X" || bordered[sR][sC]){
            return;
        }

        let visited = makeGrid();
        let current = [[sR, sC]];
        visited[sR][sC] = true;
        bordered[sR][sC] = true;
        while (current.length > 0){
            // console.log("current", current);
            let next = [];
            for (let [r, c] of current){
                for (let i = 0; i < 4; i++){
                    let nR = r + dY[i];
                    let nC = c + dX[i];

                    if (nC < 0 || nC >= n || nR < 0 || nR >= m){
                        continue;
                    }
                    if (board[nR][nC] === "X"){
                        continue;
                    }
                    if (visited[nR][nC] || bordered[nR][nC]){
                        continue;
                    }

                    visited[nR][nC] = true;
                    bordered[nR][nC] = true;
                    next.push([nR, nC]);
                }
            }
            current = next;
        }
    }

    for (let i = 0; i < n; i++){
        markBordered(0, i);
        markBordered(m-1, i);
    }
    for (let i = 0; i < m; i++){
        markBordered(i, 0);
        markBordered(i, n-1);
    }

    // console.log("markBordered");

    for (let sR = 1; sR < m-1; sR++){
        for (let sC = 1; sC < n-1; sC++){
            fill(sR, sC);
        }
    }
};
