class Trie {
    map;

    constructor() {
        this.map = {};
    }

    insert(word: string): void {
        let ptr = this.map;
        for (let i = 0; i < word.length; i++){
            let char = word[i];
            if (ptr[char] === undefined){
                ptr[char] = {};
            }
            ptr = ptr[char];
        }
        ptr["-"] = true;
        // console.log("map", this.map);
    }

    search(word: string): boolean {
        let ptr = this.map;
        for (let i = 0; i < word.length; i++){
            let char = word[i];
            if (ptr[char] === undefined){
                return false;
            }
            else {
                ptr = ptr[char];
            }
        }
        return ptr["-"] === true;
    }

    startsWith(prefix: string): boolean {
        let ptr = this.map;
        for (let i = 0; i < prefix.length; i++){
            let char = prefix[i];
            if (ptr[char] === undefined){
                return false;
            }
            else {
                ptr = ptr[char];
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
