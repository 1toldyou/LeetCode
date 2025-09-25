function wordPattern(pattern: string, s: string): boolean {
    let tokens = s.split(" ");
    let map = new Map();
    let exist = new Set();

    if (tokens.length != pattern.length){
        return false;
    }

    for (let i = 0; i < pattern.length; i++){
        let letter = pattern[i];
        let word = tokens[i];

        if (!map[letter]){
            if (exist.has(word)){
                return false;
            }

            map[letter] = word;
            exist.add(word);
        }

        if (map[letter] !== word){
            return false;
        }
    }

    return true;
};
