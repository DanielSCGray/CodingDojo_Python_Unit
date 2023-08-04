/* 
  String: Is Palindrome

  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
// function isPalindrome(str) {
//     var revStr = ''
//     for (var i = str.length - 1; i > -1; i--){
//         revStr += str[i]
//     }
//     if (revStr === str) {
//         return true
//     }
//     return false
// }

function isPalindrome(str) {
    var i = 0
    var j = str.length - 1
    while (j > i) {
        if (str[i] !== str[j]) {
            return false
        }
        i++
        j--
    }
    return true
}


console.log(isPalindrome(str1))
console.log(isPalindrome(str2))
console.log(isPalindrome(str3))
console.log(isPalindrome(str4))

/* 
  Longest Palindrome

  For this challenge, we will look not only at the entire string provided,
  but also at the substrings within it.
  Return the longest palindromic substring. 

  Strings longer or shorter than complete words are OK.

  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
// */

// const { isPalindrome } = require("../isPalindrome");

const str5 = "what up, daddy-o?";
const expected5 = "dad";

const str6 = "uh, not much";
const expected6 = "u";

const str7 = "Yikes! my favorite racecar erupted!";
const expected7 = "e racecar e";

const str8 = "a1001x20002y5677765z";
const expected8 = "5677765";

const str9 = "a1001x20002y567765z";
const expected9 = "567765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
    var longestPalin = ''
    for (var i = 0; i < str.length; i++) {
        var newStr = ''
        for (var j = i; j < str.length; j++) {
            newStr += str[j]
            if (isPalindrome(newStr)){
                if (newStr.length > longestPalin.length){
                    longestPalin = newStr
                }
            }
        }
    }
    return longestPalin
}

console.log(longestPalindromicSubstring(str5))
console.log(longestPalindromicSubstring(str6))
console.log(longestPalindromicSubstring(str7))
console.log(longestPalindromicSubstring(str8))
console.log(longestPalindromicSubstring(str9))
