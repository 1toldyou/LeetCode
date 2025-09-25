function isIsomorphic(s: string, t: string): boolean {
    let dict = new Map();
    let exist = new Set();
    for (let i = 0; i < s.length; i++){
        let a = s[i];
        let b = t[i];
        if (!dict[a]){
            if (exist.has(b)){
                return false;
            }

            dict[a] = b;
            exist.add(b);
        }

        if (dict[a] !== b){
            return false;
        }
    }
    return true;
};
