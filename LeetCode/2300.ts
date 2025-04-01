function successfulPairs(spells: number[], potions: number[], success: number): number[] {
    let potionSorted = potions.sort((a, b) => a - b);  // the default sorter seems not working 
    // console.log("potionSorted", potionSorted);
    let result = [];
    for (let spell of spells){
        // console.log("spell", spell);
        if ((spell * potionSorted[potionSorted.length-1]) < success){
            // console.log(`even the highest spell cannot satisfied`);
            result.push(0);
            continue;
        }
        
        let lowIndex = 0;
        let highIndex = potionSorted.length;
        while (lowIndex+1 < highIndex){
            let mid = lowIndex + Math.floor((highIndex-lowIndex)/2);
            // console.log("lowIndex", lowIndex, "mid", mid, "highIndex", highIndex);
            let product = spell * potionSorted[mid];
            if (product >= success){
                // console.log(`mid [${mid}]=${product} statisfy the requirement`);
                highIndex = mid;
            }
            else {
                // console.log(`mid [${mid}]=${product} less than the requirement`);
                lowIndex = mid;
            }
        }
        // console.log("spell", spell, "final lowIndex:", lowIndex);
        if (spell * potionSorted[lowIndex] >= success){
            // console.log(`[${lowIndex}] still statisfy the requirement`);
            lowIndex -= 1;
        }
        
        result.push(potionSorted.length - lowIndex - 1);
    }
    return result;
};