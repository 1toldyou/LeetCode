function isIsomorphic(s: string, t: string): boolean {
    let dict = new Map();
    for (let i = 0; i < s.length; i++){
        let a = s[i];
        let b = t[i];
        if (!dict[a]){
            dict[a] = b;
        }

        if (dict[a] !== b){
            return false;
        }
    }
    return true;
};
