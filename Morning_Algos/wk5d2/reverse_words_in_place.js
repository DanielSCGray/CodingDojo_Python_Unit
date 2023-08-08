/* 
Given a string containing space separated words
Reverse each word in the string.

If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**

Reverses the letters in each words in the given space separated
string of words. Does NOT reverse the order of the words themselves.
Time: O(?).
Space: O(?).
@param {string} str Contains space separated words.
@returns {string} The given string with each word's letters reversed.
*/

//use .split method which breaks the str into a array and reverse each string individually 
//start at the back of each string and place into a new variable, var newString = ""
//for loop 
function reverseWords(str) {
    var newString ="" 
    var arry = str.split(" ") 
    for (var i=0; i<arry.length; i++){
        tempStr = ""
        for (var j= arry[i].length-1; j>= 0; j--){ //
            tempStr += arry[i][j]
        }
        newString += tempStr 
        if (i < arry.length -1){
            newString += " "
        }
    }
    return newString
}
console.log(reverseWords(str1))
console.log(reverseWords(str2))
console.log(reverseWords(str3))