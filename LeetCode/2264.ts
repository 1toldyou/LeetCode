function largestGoodInteger(num: string): string {
    let maxNum = -1;

    let i = 0;
    while (i < num.length - 2){
        if (num[i] == num[i+1]){
            if (num[i] == num[i+2]){
                maxNum = Math.max(maxNum, parseInt(num[i]));
                i += 3;
            }
            else {
                i += 2;
            }
        }
        else {
            i++;
        }
    }

    if (maxNum > -1){
        return maxNum.toString() + maxNum.toString() + maxNum.toString(); 
    }
    
    return "";
};
