function romanToInt(s: string): number {
    const presets: any[] = [
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1]
    ];
    let result = 0;

    for (let preset of presets){
        while (true){
            if (s.startsWith(preset[0])){
                result += preset[1];
                s = s.substring(preset[0].length);
            }
            else {
                break;
            }
        }
    }

    return result;
};
