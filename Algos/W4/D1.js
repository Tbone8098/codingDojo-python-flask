/* 
  Recursively sum an arr of ints. MUST use recursion.
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
 function sumArr(nums) {
    if(nums.length == 0) return 0; // base case
    else {
      return nums[0] + sumArr(nums.slice(1));
    }
}

// **********************************************************

/* 
  Recursive Sigma
  Input: integer
  Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
 function recursiveSigma(num) {

    if(num <= 0) return 0;
    else {
      return Math.floor(num) + recursiveSigma(num-1);
    } 
    
  }


/*
  5 + recursiveSig(4)
      4 + recursiveSig(3)
          3 + recursiveSig(2)
              2 + recursiveSig(1)
                  1 + recursiveSig(0)
                      0 is returned - base case reached, can start summing now
                      - call stack "unwinds" now with .pop LIFO (matching indentation)
                  1 + 0 = 1 <- this sum becomes the right side of the next addition
              2 + 1 = 3
          3 + 3 = 6
      4 + 6 = 10
  5 + 10 = 15
*/