function binarySearch(arr, num, high = arr.length - 1, low = 0) {
    if (low > high) {
        return false;
    }

    let mid = Math.floor((high - low) / 2) + low;

    if (arr[mid] == num) {
        return true

    } else if (arr[mid] < num) {
        low = mid + 1;

    } else {
        high = mid - 1;
    }
    return binarySearch(arr, num, high, low)
}

console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))