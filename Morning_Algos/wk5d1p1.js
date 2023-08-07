/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/
//                       v
const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};
//                                                  v
const arr2 = ["a", "b", "a", "c", "Bob", "c", "c", "d"];

const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  Bob: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭
'sonara.ai'
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

console.log(makeFreqTable(arr1))
console.log(makeFreqTable(arr2))
console.log(makeFreqTable(arr3))