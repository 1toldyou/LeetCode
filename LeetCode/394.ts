function decodeString(s: string): string {
    if (s.indexOf("[") == -1){
        // console.log(s, "shall be the final stage")
        return s;
    }

    let body = "";
    let bracketCount = 0;
    let occuranceStr = "";
    let result = "";
    for (let c of s){
        // console.log("result", result, "body", body)
        switch (c){
            case "0":
            case "1":
            case "2":
            case "3":
            case "4":
            case "5":
            case "6":
            case "7":
            case "8":
            case "9":
                if (bracketCount == 0){ // before any bracket;
                    occuranceStr += c;
                }
                else {
                    body += c;
                }
                break;
            case "[":
                bracketCount += 1;
                if (bracketCount > 1){
                    body += c;
                }
                break;
            case "]":
                bracketCount -= 1;
                if (bracketCount == 0){
                    // console.log("body", body)
                    let decodedBody = decodeString(body);
                    for (let i = 0; i < parseInt(occuranceStr); i++){
                        result += decodedBody;
                    }
                    body = "";
                    occuranceStr = "";
                }
                else {
                    body += c;
                }
                break;
            default:
                if (bracketCount == 0){
                    result += c;
                }
                else {
                    body += c;
                }
        }
    }
    // console.log("decoded", result, "from", s);
    return result;
};

// function work(occurance: number, body: string): string {

// }