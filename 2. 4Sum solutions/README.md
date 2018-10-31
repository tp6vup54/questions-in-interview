# 4Sum Solutions

In this part I implement three kinds of solution, and use [leetcode](https://leetcode.com/problems/4sum/) as an assessment platform to ensure correctness and efficiency.

## Solution1 - DFS
This was the concept performed during interview, a brute force way to enumerate all the combinations.

The complexity is `combination(n, 4)`, approximately `n^4`, in which `n` is the length of `nums`.

## Solution2 - 3Sum based
After Solution1, I started to realize that it may be divided and conquered, then came up with the following thoughts.
```
for i in range(len(nums) - 3):
    3Sum(...)
```
Since under a loop, number of digits need to be found is 3, exactly the same as 3Sum.
The complexity of 3Sum is `n^2` in my solution, so the entire complexity is `n^3`.

## Solution3 - 2Sum based
This solution is almost the same as previous one, just add another nested loop.
```
for i in range(len(nums) - 3):
    for j in range(len(nums) - 2):
        2Sum(...)
```
The complexity of 2Sum is `n`, so the entire complexity is `n^3`, same as previous.

But I tried to add some little improvements to make it faster, 
