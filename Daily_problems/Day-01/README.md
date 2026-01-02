## About the Problem

**Problem Name**   : Plus One

**LeetCode ID**    : 66  

**Difficulty**     : Easy

### Example

    Input:  digits = [1, 2, 3]
    Output: [1, 2, 4]   


## Optimal Solution
Algorithm:
1. Initialize a carry variable with value 1.
2. Traverse the digits array from right to left.
3. For each digit:
   - Add the carry(Digit[i]+carry)
   - Update the digit to (sum % 10)=>(10 % 10 = 0)
   - Update carry (sum // 10) to handle overflow.
4. After loop, if a carry still exists, insert 1 at the beginning of the array.
5. Return the array.

## Working
![working](./Diagram.png)


## Complexity

Time Complexity:
O(n) – traversal of arrays

Space Complexity:
O(1) – Updating the current list itself

## Submission
![Submission](./submit.png)