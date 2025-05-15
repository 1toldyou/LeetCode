function canJump(nums: number[]): boolean {
    const findPrevZero = (end) => {
        let i = end-1;
        while (i >= 0){
            if (nums[i] === 0){
                return i;
            }
            i--;
        }
        return -1;
    }
    const canJumpOver = (zero) => {
        let offset = 1;
        while (zero - offset >= 0){
            if (nums[zero - offset] > offset){
                return true;
            }
            offset++;
        }
        return false;
    }

    let i = nums.length - 1;
    while (i >= 0){
        let prevZero = findPrevZero(i);
        if (prevZero == -1){
            return true;
        }
        // console.log("prevZero", prevZero);

        if (!canJumpOver(prevZero)){
            return false;
        }

        i = prevZero;
    }
};
