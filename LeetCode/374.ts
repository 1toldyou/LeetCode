/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */


 function guessNumber(n: number): number {
    let low = 1;
    let high = n+1;
    while (low+1 < high){
        let mid = low + Math.floor((high-low)/2);
        // console.log(low, mid, high);
        let outcome = guess(mid);
        if (outcome === 0){
            return mid;
        }
        else if (outcome > 0){
            low = mid;
        }
        else {
            high = mid;
        }
    }
    // console.log("low", low, "high", high);
    return low;
};