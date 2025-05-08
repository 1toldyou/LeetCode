function canConstruct(ransomNote: string, magazine: string): boolean {
    if (magazine.length < ransomNote.length){
        return false;
    }

    // let map = new Map();
    let map = {};
    for (let char of magazine){
        if (map[char] === undefined){
            map[char] = 0;
        }
        map[char] += 1;
    }

    for (let char of ransomNote){
        if (map[char] === undefined){
            return false;
        }
        // map[char] -= 1;

        if (--map[char] < 0){
            return false;
        }
    }

    return true;
};
