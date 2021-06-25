/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    const coins = {}
    
    if (cents >= 25){
        var quarters = Math.floor(cents/25)
        cents -= quarters * 25
        coins['quarters'] = quarters
    }
    
    if (cents >= 10){
        var dimes = Math.floor(cents/10)
        cents -= (dimes * 10)
        coins['dimes'] = dimes
    }
    
    if (cents >= 5){
        var nickels = Math.floor(cents/5)
        cents -= (nickels * 10)
        coins['nickels'] = nickels
    }
    
    if (cents > 0){
        coins['pennies'] = cents
    }
    return coins
}

console.log(fewestCoinChange(cents4));

// ************************************************************************************
// ************************************************************************************
// ************************************************************************************

/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

// const nums1 = [3, 0, 1];
// const expected1 = 2;

// const nums2 = [3, 0, 1, 2];
// const expected2 = null;
// // Explanation: nothing is missing

// /* 
//   Bonus: now the lowest value can now be any integer (including negatives),
//   instead of always being 0. 
// */

// const nums3 = [2, -4, 0, -3, -2, 1];
// const expected3 = -1;

// const nums4 = [5, 2, 7, 8, 4, 9, 3];
// const expected4 = 6;

// /**
//  * Determines what the missing int is in the given unordered array of ints
//  *    which spans from 0 to N where only one int is missing. With this missing
//  *    int, a consecutive sequence of ints could be formed from the array.
//  * Bonus: Given ints can span from N to M (start and end anywhere).
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} unorderedNums
//  * @returns {number|null} The missing integer needed to be able to form an unbroken
//  *    consecutive set of integers from the given array or null if none is missing.
//  */
// function missingValue(unorderedNums) {}