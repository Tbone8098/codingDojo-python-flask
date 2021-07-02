// /*
//   Sum To One Digit
//   Implement a function sumToOne(num)​ that,
//   given a number, sums that number’s digits
//   repeatedly until the sum is only one digit. Return
//   that final one digit result.
//   Tips:
//     to access digits from a number, need to convert it .toString() to access each digit via index
//     parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
//     isNaN(arg) used to check if something is NaN
// */

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

const num4 = 75;        // 7 + 5 = 12 || 1 + 2 = 3
const expected4 = 3;

const num4 = 175;        // 1 + 7 + 5 = 13 || 1 + 3 = 4
const expected4 = 4;

// a possibility
const num5 = -75;        // -7 + -5 = -12 || -1 + -2 = -3
const expected5 = -2;

const num5 = -28;        // -7 + 5 = -2
const expected5 = 5;

/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
function sumToOneDigit(num) {}

// **************************************************

// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129
/* 
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods

  Order of the output array does not matter!!
*/

const str1a = "lim";
const expected1a = ["ilm", "iml", "lim", "lmi", "mil", "mli"];

const str2a = "mmm";
const expected2a = ["mmm"];

const str3a = "lil";
const expected3a = ["lil", "lli", "ill"];

const str4a = "";
const expected4a = false;



/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */
function generateAnagrams(str, perms=[], partial="") {
    console.log("**********************");
    console.log(`perms: ${perms} || partial: ${partial}`);
    
    if(!str){
        perms.push(partial)
    }
    for(let i=0; i< str.length; i++){
        let leftSlice = str.slice(0, i)
        let rightSlice = str.slice(i+1) // skip current letter
        console.log(`leftSlice: ${leftSlice} || rightSlice: ${rightSlice}`);
        generateAnagrams(leftSlice + rightSlice, perms, partial+str[i])
    }
    return perms
}

console.log(generateAnagrams(str1a));