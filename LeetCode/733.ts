function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    let startingColor = image[sr][sc];
    image[sr][sc] = color;
    const isCoordValid = (row, col) => {
        return row >= 0 && row < image.length && col >= 0 && col < image[0].length;
    }

    let visited = new Array(image.length);
    for (let row = 0; row < image.length; row++){
        visited[row] = (new Array(image[0].length).fill(false));
    }
    visited[sr][sc] = true;
    let currentBatch = [[sr, sc]];
    while (currentBatch.length > 0){
        // console.log("currentBatch", currentBatch);
        let nextBatch = [];
        for (let coord of currentBatch){
            for (let next of [[coord[0]+1, coord[1]], [coord[0]-1, coord[1]], [coord[0], coord[1]+1], [coord[0], coord[1]-1]]){
                if (!isCoordValid(next[0], next[1])){
                    continue;
                }
                if (image[next[0]][next[1]] !== startingColor){
                    continue;
                }
                if (visited[next[0]][next[1]]){
                    continue;
                }

                image[next[0]][next[1]] = color;
                visited[next[0]][next[1]] = true;
                nextBatch.push([next[0], next[1]]);
            }
        }
        currentBatch = nextBatch;
    }

    return image;
};
