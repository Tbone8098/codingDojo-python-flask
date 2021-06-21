/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visited indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1];
// const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0];
// const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1];
// const expected2 = false;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */


function socialDistancingEnforcer(queue) {
    let counter = 6
    for (let i=0; i<queue.length; i++){
        if (queue[i] === 1){
            if(counter < 6){
                return false
            }

            counter = 0
        } else {
            counter++
        }
    }
    return true
}

console.log(socialDistancingEnforcer(queue2));

// *****************************************************************************

/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2; // index location

const nums2 = [9, 9];
const expected2 = -1;

const nums3 = [3,0,1,2];
const expected3 = 1;
/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */

// O(2n)
function balanceIndex(nums) {

    let left = 0;
    let totalSum = nums.reduce((a,b)=> a+b);
    
    for(let i=1; i<nums.length; i++) {
        left += nums[i-1];
        let right = totalSum - nums[i] - left;
        if(left == right) { 
        return i;
        } 
    }
    return -1;
    }

/**
 * - Time: O(2n) linear -> O(n).
 * - Space: O(1) constant.
 */
 function balanceIndex(nums) {
    if (nums.length < 3) {
      return -1;
    }
  
    let left = nums[0];
    let right = 0;
  
    for (let i = 2; i < nums.length; i++) {
      right += nums[i];
    }
  
    for (let i = 1; i < nums.length - 1; i++) {
      if (left === right) {
        return i;
      }
  
      right -= nums[i + 1];
      left += nums[i];
    }
    return -1;
  }

  /**
 * - Time: O(n/2) -> O(n) linear, n/2 since looping from outside towards center.
 * - Space: O(1) constant.
 */
function balanceIndexOutsideIn(nums) {
    if (nums.length < 3) {
      return -1;
    }
    let leftIdx = 0;
    let rightIdx = nums.length - 1;
    let leftSum = 0;
    let rightSum = 0;
  
    while (leftIdx < rightIdx) {
      if (nums[leftIdx] == 0) {
        leftIdx++;
        continue;
      }
      if (nums[rightIdx] == 0) {
        rightIdx--;
        continue;
      }

      if (leftSum == rightSum) {
        leftSum += nums[leftIdx];
        rightSum += nums[rightIdx];
        leftIdx++;
        rightIdx--;

      } else if (leftSum < rightSum) {
        leftSum += nums[leftIdx];
        leftIdx++;

      } else {
        rightSum += nums[rightIdx];
        rightIdx--;
      }
    }
  
    if (leftSum == rightSum && leftIdx == rightIdx) {
      return leftIdx;
    } else {
      return -1;
    }
  }