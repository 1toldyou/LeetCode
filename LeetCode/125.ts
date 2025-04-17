function isPalindrome(s: string): boolean {
    s = s.toLowerCase()
        .replaceAll(" ", "")
        .replaceAll(/\W/g, "")
        .replaceAll("_", "")
    // console.log(s);
    let a = 0;
    let b = s.length - 1;
    while (a < b){
        // console.log(a, b, s[a], s[b]);
        if (s[a] !== s[b]){
            return false;
        }
        a++;
        b--;
    }
    return true;
};
