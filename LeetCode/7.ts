function reverse(x: number): number {
    if (x === 0){
        return 0;
    }

    let isNegative: boolean = x < 0;
    if (isNegative){
        x = x * -1;
    } 
    let str = x.toString();
    // console.log("str", str);
    let revStr = str.split("").reverse().join("");
    // console.log("revStr", revStr);
    let nonZeroIndex = 0;
    for (let i = 0; i < revStr.length; i++){
        if (revStr[i] === "0"){
            nonZeroIndex++;
        }
        else {
            break;
        }
    }
    let noZeroRevStr = revStr.substring(nonZeroIndex);
    // console.log("noZeroRevStr", noZeroRevStr);

    // TODO: check for overflow
    let maxStr = (Math.pow(2, 31) - (isNegative ? 0 : 1)).toString();
    // console.log("maxStr", maxStr);
    if (noZeroRevStr.length > maxStr.length){
        // console.log("noZeroRevStr.length > maxStr.length")
        return 0;
    }
    else if (noZeroRevStr.length === maxStr.length){
        for (let i = 0; i < noZeroRevStr.length; i++){
            // console.log(`i=${i}`, parseInt(noZeroRevStr[i]), parseInt(maxStr[i]))
            if (parseInt(noZeroRevStr[i]) > parseInt(maxStr[i])){
                // console.log(`parseInt(noZeroRevStr[${i}]) ${parseInt(noZeroRevStr[i])} > parseInt(maxStr[${i}]) ${parseInt(maxStr[i])}`);
                return 0;
            }
            else if (parseInt(noZeroRevStr[i]) < parseInt(maxStr[i])){
                break;
            }
        }
    }

    let sign: string = isNegative ? "-" : "";
    return parseInt(sign + noZeroRevStr);
};
