/* 
  String Decode  
*/

const str1 = 'a3b2c1d3';
const expected1 = 'aaabbcddd';

const str2 = 'a3b2c12d10';
const expected2 = 'aaabbccccccccccccdddddddddd';

const str3 = 'c12d10'

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {
    var newStr = ''
    var char = ''
    var num = 0
    for (var i = 0; i < str.length; i+=2){
        char = str[i]
        num = Number(str[i+1])
        for (var j = 0; j < num; j++){
            newStr += char
        }
    }
    return newStr
}

console.log(decodeStr(str1))

function decodeStr2(str) {
    var newStr = ''
    var char = ''
    var num = 0
    var numStr = ''
    for (var i = 0; i < str.length; i++){
        if (isNaN(str[i])){
            char = str[i]
            continue
        }
        numStr += str[i];
        console.log(numStr)
        if (isNaN(str[i+1]) === false){
            continue
        }
        
        num = Number(numStr)
        // console.log(num)
        for (var j = 0; j < num; j++){
            newStr += char
        }
        numStr = ''
    }
    return newStr
}
console.log(decodeStr2(str1))
console.log(decodeStr2(str2))
// console.log(decodeStr2(str3))