/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected1 = 1;

//               v
const nums2 = [5, 4, 5];
const expected2 = 4;

//                                V
const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// pseudocode here

// create the function and decide what params it needs and what it will return
function makeFreqTable(array){
    var newObj = {}
    for (let i = 0; i < array.length; i++) {
        if (String(array[i]) in newObj){
            newObj[String(array[i])] += 1
        }
        else {
            newObj[String(array[i])] = 1
        }
    }
    return newObj
}

function getOdd(arr){
    var table = makeFreqTable(arr)
    for (key in table) {
        if (table[key] % 2 === 1){
            return key
        }
    }
    return 'All numbers occur an even amount.'
}
console.log(getOdd(nums1))
console.log(getOdd(nums2))
console.log(getOdd(nums3))
console.log(getOdd(nums4))