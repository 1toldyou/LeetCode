/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let resultLength = m + n;
    let result = new Array(resultLength);
    let a = 0;
    let b = 0;
    for (let i = 0; i < resultLength; i++){
        // console.log(result);
        if (a < m && b < n){
            if (nums1[a] < nums2[b]){
                result[i] = nums1[a++]
            }
            else {
                result[i] = nums2[b++]
            }
        }
        else if (a < m){
            result[i] = nums1[a++]
        }
        else if (b < n) {  // 
            result[i] = nums2[b++]
        }
        else {

        }
    }
    // console.log("result", result)
    for (let i = 0; i < nums1.length; i++){
        nums1[i] = result[i];
    }
};
