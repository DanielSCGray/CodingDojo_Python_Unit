const nums6 = [1, 2, 3];
const expected6 = 6;

const nums7 = [1];
const expected7 = 1;

const nums8 = [];
const expected8 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums) {
    if (nums.length == 0) {
        return 0;
    }

    let x = nums.pop();

    return sumArr(nums) + x;
}
console.log("************************");
console.log(sumArr(nums6), "should be", expected6);
console.log(sumArr(nums7), "should be", expected7);
console.log(sumArr(nums8), "should be", expected8);