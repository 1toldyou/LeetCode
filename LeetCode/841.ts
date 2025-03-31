function canVisitAllRooms(rooms: number[][]): boolean {
    let visited: boolean[] = [];
    // for (let i = 0; i < rooms.length; i++){
    //     visit(rooms, i, visited);
    // }
    visit(rooms, 0, visited);

    // console.log("visited", visited);
    if (visited.length != rooms.length){
        return false;
    }
    // return visited.every((x) => x === true)
    for (let i = 0; i < visited.length; i++){
        if (visited[i] !== true){
            return false;
        }
    }
    return true;
};

function visit(rooms: number[][], roomNum: number, visited: boolean[]){
    if (visited[roomNum] === true) {

    } else {
        visited[roomNum] = true;
        for (let subRoom of rooms[roomNum]){
            // console.log("from", roomNum, "can visit", subRoom);
            visit(rooms, subRoom, visited);
        }
    }
}