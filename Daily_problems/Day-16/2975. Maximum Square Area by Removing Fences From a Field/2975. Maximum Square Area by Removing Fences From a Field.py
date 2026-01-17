"""
Problem Name   : Maximum Square Area by Removing Fences From a Field
LeetCode ID    : 2975
Difficulty     : Medium

Problem Statement:
------------------
Return the maximum area of a square field that can be formed by removing some fences.

Example:
--------
Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.
"""

"""
Algorithm:
----------
1. Add the field boundaries to hfence(1->m) and vfence(1->n).
2. Calc all possible distances between pairs of horizontal fences and store them in a set.
3. Compute all possible distances between pairs of vertical fences.
4. Find the largest distance that appears in both horizontal and vertical distance sets.
5. If no common distance -> -1; o.w -> square area
"""

# solution
m = 4
n = 3
hFences = [2,3]
vFences = [2]
M = 10**9+7
# fences -> (1,1) to (m,n) -> (height, width)
hFences.extend([1,m]) 
vFences.extend([1,n])

# hash set to store diff
hash_set = set()
side = 0

# finding horizontal gaps
h = len(hFences)
for i in range(h):
    for j in range(i+1, h):
        hash_set.add(abs(hFences[j]-hFences[i]))

# finding horizontal gaps
w = len(vFences)
for i in range(w):
    for j in range(i+1, w):
        hdiff = abs(abs(vFences[j]-vFences[i]))
        if hdiff in hash_set:
            side = max(side, hdiff)

# impossible to make a square field            
if side == 0:
    print(-1)

# if possible
print((side * side) % M) # (2 * 2) % 10**9+7

"""
Time Complexity:
----------------
O(H^2 + V^2) - Iterating through pairs of fences

Space Complexity:
-----------------
Space: O(H^2) - Hash set
"""
