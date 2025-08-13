function searchRange(nums: number[], target: number): number[] {
    let arrSize = nums.length;
    if (arrSize == 0){
        return [-1,-1];
    }

    if (arrSize == 1 && nums[0] == target){
        return [0, 0];
    }

    let low = 0;
    let high = arrSize - 1;
    while(high >= low){
        let mid = low + Math.floor((high - low) / 2);

        if (nums[mid] == target){
            let start = mid;
            let end = mid;
            while(start > 0){
                if (nums[start-1] == target){
                    start--;
                }
                else {
                    break;
                }
            }
            while(end < arrSize - 1){
                if (nums[end+1] == target){
                    end++;
                }
                else {
                    break;
                }
            }

            return [start, end];
        }
        if (nums[mid] < target){
            low = mid + 1;
        }
        if (nums[mid] > target){
            high = mid - 1;
        }
    }

    return [-1,-1];
};
