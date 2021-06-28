/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Do it in-place in O(n) time and no new array
  Bonus: Keep it O(n) time even if it is not sorted
*/

// const nums1 = [1, 1, 1, 1];
// const expected1 = [1];

// const nums2 = [1, 1, 2, 2, 3, 3];
// const expected2 = [1, 2, 3];

// const nums3 = [1, 1, 2, 3, 3, 4];
// const expected3 = [1, 2, 3, 4];

// const nums4 = [1, 1];
// const expected4 = [1];

// /**
//  * De-dupes the given sorted array.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} nums
//  * @returns {Array<number>} The given array deduped.
//  */
// function dedupeSorted(nums) {}


// **********************************************************

/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
  what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

const nums6 = [5, 1, 1, 5];
const expected6 = [];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    var freq = {}
    var maxFreq = 0
    var allSame = true

    for (var n of nums){
        freq.hasOwnProperty(n) ? freq[n] += 1 : freq[n] = 1
        // if (freq.hasOwnProperty(n)){
        //     freq[n] += 1
        // } else {
        //     freq[n] = 1
        // }

        if (freq[n] > maxFreq){
            maxFreq = freq[n]
        }
    }
    console.log(maxFreq);
    console.log(freq);
    var returnList = []
    for (var key in freq){
        if (freq[key] === maxFreq){
            returnList.push(parseInt(key))
        } else {
            allSame = false
        }
    }
    return allSame ? [] : returnList
}

console.log(mode(nums6));