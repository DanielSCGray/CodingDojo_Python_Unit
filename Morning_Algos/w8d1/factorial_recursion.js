const num1 = 3;
const expected1 = 6;
// Explanation: 1 * 2 * 3 = 6

const num2 = 5;
const expected2 = 120;
// Explanation: 1 * 2 * 3 * 4 * 5 = 120

const num3 = 3.5;
const expected3 = 6;
// Explanation: 1 * 2 * 3 = 6

const num4 = 0;
const expected4 = -1;
// Explanation: num is zero, return -1

const num5 = -1;
const expected5 = -1;
// Explanation: num is less than zero, return -1

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function rFactorial(num) {
  // pseudo code
  num = Math.floor(num);
  if (num == 1) {
    return 1;
  }
  if (num <= 0) {
    return -1;
  }

  return rFactorial(num - 1) * num;

  // base case
  // progression
  // call itself
}

console.log(rFactorial(num1), "should be", expected1);
console.log(rFactorial(num2), "should be", expected2);
console.log(rFactorial(num3), "should be", expected3);
console.log(rFactorial(num4), "should be", expected4);
console.log(rFactorial(num5), "should be", expected5);