# Binary Search

## Complexity

- Best: O(n log n)
- Worst: O(n log n)
- Avg: O(n log n)
- Space: O(n)

## Problem Description

This page demonstrates binary search on a sorted copy of an input array. Binary search is one of the classic divide-and-conquer search algorithms because it never checks values one by one from left to right. Instead, it repeatedly compares the target against the middle value of the current search range and then discards the half that cannot possibly contain the answer. That repeated halving is what makes binary search so efficient when the input is already ordered.

In this example, however, the input does not begin in sorted order. Because of that, the program first makes a copy of the original array, sorts that copy with merge sort, and only then runs binary search on the sorted result. That means the page is showing the full process needed for this specific implementation, not binary search in isolation.

## Code

```javascript
/**
 * Perform binary search on a sorted array and return the target index.
 *
 * @param {number[]} values Sorted input array.
 * @param {number} target Value to locate.
 * @returns {number} Index of the target in the sorted array, or -1 if absent.
 */
function binarySearch(values, target) {
    let low = 0;
    let high = values.length - 1;

    while (low <= high) {
        // Recompute the midpoint for the current search range.
        const mid = Math.floor((low + high) / 2);

        if (values[mid] === target) {
            return mid;
        }

        // Discard the half that cannot contain the target.
        if (target > values[mid]) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;
}

/**
 * Sort an array with merge sort and return a new sorted array.
 *
 * @param {number[]} values Input array.
 * @returns {number[]} Sorted copy of the input values.
 */
function mergeSort(values) {
    if (values.length <= 1) {
        return values;
    }

    const mid = Math.floor(values.length / 2);
    const left = mergeSort(values.slice(0, mid));
    const right = mergeSort(values.slice(mid));

    return merge(left, right);
}

/**
 * Merge two sorted arrays into one sorted array.
 *
 * @param {number[]} left Left sorted half.
 * @param {number[]} right Right sorted half.
 * @returns {number[]} Merged sorted output.
 */
function merge(left, right) {
    const sorted = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] <= right[rightIndex]) {
            sorted.push(left[leftIndex]);
            leftIndex++;
        } else {
            sorted.push(right[rightIndex]);
            rightIndex++;
        }
    }

    // Append whichever half still contains unmerged values.
    return sorted.concat(left.slice(leftIndex), right.slice(rightIndex));
}

/**
 * Run the binary-search demonstration with a sorted copy of an unsorted array.
 *
 * @returns {void}
 */
function main() {
    const array = [4, 67, 20, 88, 10, 83];
    const sortedArray = mergeSort([...array]);
    const randomIndex = Math.floor(Math.random() * array.length);
    const target = array[randomIndex];

    console.log("Original array =", array);
    console.log("Sorted array =", sortedArray);
    console.log("Target =", target);
    console.log("Found index in sorted array =", binarySearch(sortedArray, target));
}

main();
```

## Algorithm Steps

1. Copy the original array and sort that copy with merge sort so the data satisfies binary search's sorted input requirement.
2. Initialize `low` to the first index and `high` to the last index of the sorted array.
3. Compute the middle index of the current search range.
4. If the middle value matches the target, return that index from the sorted array.
5. If the target is smaller than the middle value, move the search range left by setting `high = mid - 1`.
6. If the target is larger than the middle value, move the search range right by setting `low = mid + 1`.
7. Repeat until the target is found or the search range becomes empty.

## Explanation

The key requirement for binary search is that the data must already be sorted. Once that condition is true, the algorithm is very efficient because each comparison with the middle value removes half of the remaining search range. That is why binary search by itself runs in `O(log n)` time.

In this implementation, though, the full program does more than just search. It first uses merge sort to turn the unsorted input into a sorted copy. That sorting step takes `O(n log n)` time and `O(n)` extra space. After that, binary search runs on the sorted array and returns the position of the target inside that sorted version of the data, not its original position in the unsorted array.

Because merge sort is more expensive than binary search, the sorting work dominates the overall runtime. That is why the complexity shown on this page is `O(n log n)` for the full example, even though the actual binary search step is only `O(log n)`.
