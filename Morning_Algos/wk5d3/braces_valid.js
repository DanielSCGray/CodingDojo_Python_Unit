/* 
Braces Valid

Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var curl_count = 0
    var square_count = 0
    var par_count = 0
    for (char of str) {
        if (char == '(') {
            par_count++
        }
        else if (char == ')') {
            par_count--
        }
        else if (char == '{') {
            curl_count++
        }
        else if (char == '}') {
            curl_count--
        }
        else if (char == '[') {
            square_count++
        }
        else if (char == ']') {
            square_count--
        }
        if (par_count < 0 || curl_count < 0 || square_count < 0) {
            return false
        }
        
    }
    if (par_count + curl_count + square_count == 0) {
        return true
    }
    return false
}

console.log(bracesValid(str1))
console.log(bracesValid(str2))
console.log(bracesValid(str3))