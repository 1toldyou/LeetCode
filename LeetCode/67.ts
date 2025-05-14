function addBinary(a: string, b: string): string {
    let maxLength = Math.max(a.length, b.length);
    a = a.padStart(maxLength, "0");
    b = b.padStart(maxLength, "0");
    // console.log("a", a);
    // console.log("b", b);
    // let result = "".padStart(maxLength+1, "0");
    let result = (new Array(maxLength+1)).fill("0");
    // console.log("result", result);

    for (let i = maxLength-1; i >= 0; i--){
        // console.log(i, "a[i]", a[i], "b[i]", b[i], "result[i+1]", result[i+1])
        let comp = parseInt(a[i]) + parseInt(b[i]) + parseInt(result[i+1]);
        switch(comp){
            case 0:
                break;
                result[i+1] = "0";
            case 1:
                result[i+1] = "1";
                break;
            case 2:
                result[i+1] = "0";
                result[i] = "1";
                break;
            case 3:
                result[i+1] = "1";
                result[i] = "1";
                break;
        }
    }

    let final = result.join("");
    if (final[0] === "0"){
        return final.substring(1);
    }
    else {
        return final;
    }
};
