function letterCombinations(digits: string): string[] {
    if (digits === ""){
        return [];
    }

    let current = [];
    for (let digit of digits){
        if (current.length === 0){
            current = digitToLetters(digit);
        }
        else {
            let newLetters = digitToLetters(digit);
            let newCombos = [];
            for (let oldCombo of current){
                for (let newLetter of newLetters){
                    newCombos.push(oldCombo + newLetter);
                }
            }
            current = newCombos;
        }
    }
    return current;
};

function digitToLetters(digit: string): string[]{
    switch(digit){
        case "2":
            return ["a", "b", "c"];
        case "3":
            return ["d", "e", "f"];
        case "4":
            return ["g", "h", "i"];
        case "5":
            return ["j", "k", "l"];
        case "6":
            return ["m", "n", "o"];
        case "7":
            return ["p", "q", "r", "s"];
        case "8":
            return ["t", "u", "v"];
        case "9":
            return ["w", "x", "y", "z"];
        default:
            return [];
    }
}