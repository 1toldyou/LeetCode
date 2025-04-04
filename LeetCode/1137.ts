function tribonacci(n: number): number {
    if (n <= 0){
        return 0;
    }
    if (n === 1 || n === 2 ){
        return 1;
    };

    let last3 = 0;
    let last2 = 1;
    let last1 = 1;
    let trib = 0;
    for (let i = 3; i <= n; i++){
        trib = last3 + last2 + last1;
        last3 = last2;
        last2 = last1;
        last1 = trib;
        // console.log(i, trib);
    }
    return trib;
};